import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-secreta-muy-segura'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'tu_usuario'
    MYSQL_PASSWORD = 'tu_contraseña'
    MYSQL_DB = 'coleccion_musical'
    MYSQL_CURSORCLASS = 'DictCursor'