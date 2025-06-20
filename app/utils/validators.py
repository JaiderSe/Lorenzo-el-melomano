import re
from flask import flash

def validate_email(email):
    """
    Valida que el email tenga un formato correcto
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        flash('El formato del email no es válido', 'danger')
        return False
    return True

def validate_password(password):
    """
    Valida que la contraseña cumpla con los requisitos de seguridad
    """
    if len(password) < 8:
        flash('La contraseña debe tener al menos 8 caracteres', 'danger')
        return False
    if not any(char.isdigit() for char in password):
        flash('La contraseña debe contener al menos un número', 'danger')
        return False
    if not any(char.isupper() for char in password):
        flash('La contraseña debe contener al menos una letra mayúscula', 'danger')
        return False
    return True

def validate_year(year):
    """
    Valida que el año sea válido (entre 1900 y el año actual + 1)
    """
    from datetime import datetime
    current_year = datetime.now().year
    try:
        year_int = int(year)
        if 1900 <= year_int <= current_year + 1:
            return True
        flash(f'El año debe estar entre 1900 y {current_year + 1}', 'danger')
        return False
    except ValueError:
        flash('El año debe ser un número válido', 'danger')
        return False