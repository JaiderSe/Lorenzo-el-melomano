from functools import wraps
from flask import redirect, url_for, flash, session

def login_required(f):
    """
    Decorador que asegura que el usuario esté logueado.
    Si no está logueado, redirige a la página de login.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'id_usuario' not in session:
            flash('Por favor inicia sesión para acceder a esta página', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """
    Decorador que verifica si el usuario es administrador.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('es_admin', False):
            flash('No tienes permisos para acceder a esta página', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function