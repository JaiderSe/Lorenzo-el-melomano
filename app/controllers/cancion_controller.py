from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.cancion import Cancion
from app.models.album import Album
from app.utils.decorators import login_required
from app.utils.helpers import format_duration, parse_duration

cancion_bp = Blueprint('cancion', __name__, url_prefix='/albumes/<int:id_album>/canciones')

@cancion_bp.route('/')
@login_required
def listar(id_album):
    """
    Lista todas las canciones de un álbum
    """
    # Verificar que el álbum pertenezca al usuario
    album = Album.get_by_id(id_album)
    if not album or album['id_usuario'] != session['id_usuario']:
        flash('Álbum no encontrado o no tienes permisos', 'danger')
        return redirect(url_for('album.listar'))
    
    canciones = Cancion.get_by_album(id_album)
    # Formatear la duración para mostrar en formato MM:SS
    for cancion in canciones:
        cancion['duracion_formateada'] = format_duration(cancion['duracion'])
    
    return render_template('canciones/list.html', canciones=canciones, album=album)

@cancion_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear(id_album):
    """
    Crea una nueva canción en un álbum
    """
    # Verificar que el álbum pertenezca al usuario
    album = Album.get_by_id(id_album)
    if not album or album['id_usuario'] != session['id_usuario']:
        flash('Álbum no encontrado o no tienes permisos', 'danger')
        return redirect(url_for('album.listar'))
    
    if request.method == 'POST':
        titulo = request.form['titulo'].strip()
        duracion_str = request.form['duracion']
        interprete = request.form['interprete'].strip()
        
        if not titulo:
            flash('El título de la canción es requerido', 'danger')
            return redirect(url_for('cancion.crear', id_album=id_album))
        
        try:
            duracion = parse_duration(duracion_str)
        except ValueError:
            flash('Formato de duración inválido. Use MM:SS', 'danger')
            return redirect(url_for('cancion.crear', id_album=id_album))
        
        Cancion.create(id_album, titulo, duracion, interprete)
        flash('Canción añadida exitosamente', 'success')
        return redirect(url_for('cancion.listar', id_album=id_album))
    
    return render_template('canciones/create.html', album=album)

@cancion_bp.route('/editar/<int:id_cancion>', methods=['GET', 'POST'])
@login_required
def editar(id_album, id_cancion):
    """
    Edita una canción existente
    """
    # Verificar permisos del álbum
    album = Album.get_by_id(id_album)
    if not album or album['id_usuario'] != session['id_usuario']:
        flash('Álbum no encontrado o no tienes permisos', 'danger')
        return redirect(url_for('album.listar'))
    
    cancion = Cancion.get_by_id(id_cancion)
    if not cancion or cancion['id_album'] != id_album:
        flash('Canción no encontrada', 'danger')
        return redirect(url_for('cancion.listar', id_album=id_album))
    
    if request.method == 'POST':
        titulo = request.form['titulo'].strip()
        duracion_str = request.form['duracion']
        interprete = request.form['interprete'].strip()
        
        if not titulo:
            flash('El título de la canción es requerido', 'danger')
            return redirect(url_for('cancion.editar', id_album=id_album, id_cancion=id_cancion))
        
        try:
            duracion = parse_duration(duracion_str)
        except ValueError:
            flash('Formato de duración inválido. Use MM:SS', 'danger')
            return redirect(url_for('cancion.editar', id_album=id_album, id_cancion=id_cancion))
        
        Cancion.update(id_cancion, titulo_cancion=titulo, duracion=duracion, interprete=interprete)
        flash('Canción actualizada exitosamente', 'success')
        return redirect(url_for('cancion.listar', id_album=id_album))
    
    # Convertir duración a formato MM:SS para el formulario
    cancion['duracion_form'] = format_duration(cancion['duracion'])
    return render_template('canciones/edit.html', album=album, cancion=cancion)

@cancion_bp.route('/eliminar/<int:id_cancion>', methods=['POST'])
@login_required
def eliminar(id_album, id_cancion):
    """
    Elimina una canción
    """
    # Verificar permisos del álbum
    album = Album.get_by_id(id_album)
    if not album or album['id_usuario'] != session['id_usuario']:
        flash('Álbum no encontrado o no tienes permisos', 'danger')
        return redirect(url_for('album.listar'))
    
    cancion = Cancion.get_by_id(id_cancion)
    if not cancion or cancion['id_album'] != id_album:
        flash('Canción no encontrada', 'danger')
        return redirect(url_for('cancion.listar', id_album=id_album))
    
    Cancion.delete(id_cancion)
    flash('Canción eliminada exitosamente', 'success')
    return redirect(url_for('cancion.listar', id_album=id_album))

@cancion_bp.route('/buscar')
@login_required
def buscar(id_album):
    """
    Busca canciones dentro de un álbum
    """
    album = Album.get_by_id(id_album)
    if not album or album['id_usuario'] != session['id_usuario']:
        flash('Álbum no encontrado o no tienes permisos', 'danger')
        return redirect(url_for('album.listar'))
    
    query = request.args.get('q', '').strip()
    if not query:
        return redirect(url_for('cancion.listar', id_album=id_album))
    
    canciones = Cancion.search_by_title(query)
    # Filtrar solo las canciones de este álbum
    canciones = [c for c in canciones if c['id_album'] == id_album]
    
    # Formatear la duración
    for cancion in canciones:
        cancion['duracion_formateada'] = format_duration(cancion['duracion'])
    
    return render_template('canciones/list.html', canciones=canciones, album=album, query=query)