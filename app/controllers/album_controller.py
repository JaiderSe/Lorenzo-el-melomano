from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.album import Album
from app.models.artista import Artista
from app.models.cancion import Cancion
from app.utils.decorators import login_required

album_bp = Blueprint('album', __name__, url_prefix='/albums')

@album_bp.route('/')
@login_required
def listar():
    id_usuario = session.get('id_usuario')
    if not id_usuario:
        flash('Usuario no autenticado', 'danger')
        return redirect(url_for('auth.login'))
    albums = Album.get_by_user(id_usuario)
    print(albums)
    return render_template('albums/list.html', albums=albums)

@album_bp.route('/<int:id_album>')
@login_required
def detalle(id_album):
    album = Album.get_by_id(id_album)
    if not album or album['id_usuario'] != session['id_usuario']:
        flash('Álbum no encontrado o no tienes permisos', 'danger')
        return redirect(url_for('album.listar'))
    
    artistas = Artista.get_by_album(id_album)
    canciones = Cancion.get_by_album(id_album)
    return render_template('albums/detail.html', album=album, artistas=artistas, canciones=canciones)

@album_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        ano_produccion = request.form['ano_produccion']
        descripcion = request.form['descripcion']
        medio = request.form['medio']
        id_usuario = session['id_usuario']
        
        id_album = Album.create(id_usuario, titulo, ano_produccion, descripcion, medio)
        flash('Álbum creado exitosamente', 'success')
        return redirect(url_for('album.detalle', id_album=id_album))
    
    return render_template('albums/create.html')

@album_bp.route('/editar/<int:id_album>', methods=['GET', 'POST'])
@login_required
def editar(id_album):
    album = Album.get_by_id(id_album)
    if not album or album['id_usuario'] != session['id_usuario']:
        flash('Álbum no encontrado o no tienes permisos', 'danger')
        return redirect(url_for('album.listar'))
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        ano_produccion = request.form['ano_produccion']
        descripcion = request.form['descripcion']
        medio = request.form['medio']
        
        Album.update(id_album, titulo, ano_produccion, descripcion, medio)
        flash('Álbum actualizado exitosamente', 'success')
        return redirect(url_for('album.detalle', id_album=id_album))
    
    return render_template('albums/edit.html', album=album)

@album_bp.route('/eliminar/<int:id_album>', methods=['POST'])
@login_required
def eliminar(id_album):
    album = Album.get_by_id(id_album)
    if not album or album['id_usuario'] != session['id_usuario']:
        flash('Álbum no encontrado o no tienes permisos', 'danger')
        return redirect(url_for('album.listar'))
    
    Album.delete(id_album)
    flash('Álbum eliminado exitosamente', 'success')
    return redirect(url_for('album.listar'))