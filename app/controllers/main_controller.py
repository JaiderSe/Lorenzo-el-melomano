from flask import Blueprint, render_template, redirect, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def inicio():
    # return redirect(url_for('auth.login'))  # Redirige a login por defecto
    # O si prefieres una página de inicio:
    return render_template('index.html')