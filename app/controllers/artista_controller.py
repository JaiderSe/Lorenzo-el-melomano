from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.artista import Artista
from app.models.album import Album
from app.utils.decorators import login_required

artista_bp = Blueprint('artista', __name__, url_prefix='/artistas')

@artista_bp.route('/')
@login_required
def listar():
    """
    Lista todos los artistas disponibles
    """
    artistas = Artista.get_all()
    return render_template('artistas/list.html', artistas=artistas)

@artista_bp.route('/<int:id_artista>')
@login_required
def detalle(id_artista):
    """
    Muestra el detalle de un artista y los álbumes asociados
    """
    artista = Artista.get_by_id(id_artista)
    if not artista:
        flash('Artista no encontrado', 'danger')
        return redirect(url_for('artista.listar'))
    
    # Obtener álbumes del artista que pertenecen al usuario actual
    albumes = Album.get_by_artist_and_user(id_artista, session['id_usuario'])
    
    return render_template('artistas/detail.html', artista=artista, albumes=albumes)

@artista_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    """
    Crea un nuevo artista
    """
    if request.method == 'POST':
        nombre_artista = request.form['nombre_artista'].strip()
        
        if not nombre_artista:
            flash('El nombre del artista es requerido', 'danger')
            return redirect(url_for('artista.crear'))
        
        # Verificar si el artista ya existe
        existente = Artista.get_by_name(nombre_artista)
        if existente:
            flash('Este artista ya existe', 'info')
            return redirect(url_for('artista.detalle', id_artista=existente[0]['id_artista']))
        
        id_artista = Artista.create(nombre_artista)
        flash('Artista creado exitosamente', 'success')
        return redirect(url_for('artista.detalle', id_artista=id_artista))
    
    return render_template('artistas/create.html')

@artista_bp.route('/editar/<int:id_artista>', methods=['GET', 'POST'])
@login_required
def editar(id_artista):
    """
    Edita un artista existente
    """
    artista = Artista.get_by_id(id_artista)
    if not artista:
        flash('Artista no encontrado', 'danger')
        return redirect(url_for('artista.listar'))
    
    if request.method == 'POST':
        nombre_artista = request.form['nombre_artista'].strip()
        
        if not nombre_artista:
            flash('El nombre del artista es requerido', 'danger')
            return redirect(url_for('artista.editar', id_artista=id_artista))
        
        Artista.update(id_artista, nombre_artista)
        flash('Artista actualizado exitosamente', 'success')
        return redirect(url_for('artista.detalle', id_artista=id_artista))
    
    return render_template('artistas/edit.html', artista=artista)

@artista_bp.route('/eliminar/<int:id_artista>', methods=['POST'])
@login_required
def eliminar(id_artista):
    """
    Elimina un artista (solo si no tiene álbumes asociados)
    """
    # Verificar si el artista tiene álbumes asociados
    albumes = Album.get_by_artist(id_artista)
    if albumes:
        flash('No puedes eliminar este artista porque tiene álbumes asociados', 'danger')
        return redirect(url_for('artista.detalle', id_artista=id_artista))
    
    Artista.delete(id_artista)
    flash('Artista eliminado exitosamente', 'success')
    return redirect(url_for('artista.listar'))

@artista_bp.route('/buscar')
@login_required
def buscar():
    """
    Busca artistas por nombre
    """
    query = request.args.get('q', '').strip()
    if not query:
        return redirect(url_for('artista.listar'))
    
    artistas = Artista.get_by_name(query)
    return render_template('artistas/list.html', artistas=artistas, query=query)