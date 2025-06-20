from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        
        if Usuario.get_by_nombre(nombre):
            flash('El nombre de usuario ya existe', 'danger')
            return redirect(url_for('auth.registro'))
        
        hashed_password = generate_password_hash(contrasena)
        Usuario.create(nombre, hashed_password)
        flash('Registro exitoso. Por favor inicia sesión.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        
        usuario = Usuario.get_by_nombre(nombre)
        if usuario and check_password_hash(usuario['contrasena'], contrasena):
            session['id_usuario'] = usuario['id_usuario']
            session['nombre'] = usuario['nombre']
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('album.listar'))
        
        flash('Nombre de usuario o contraseña incorrectos', 'danger')
    
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('auth.login'))