from flask import Flask
from flask_mysqldb import MySQL
from app.config import Config

mysql = MySQL()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    mysql.init_app(app)
    
    # Registrar blueprints
    from app.controllers.auth_controller import auth_bp
    from app.controllers.album_controller import album_bp
    from app.controllers.artista_controller import artista_bp
    from app.controllers.cancion_controller import cancion_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(album_bp)
    app.register_blueprint(artista_bp)
    app.register_blueprint(cancion_bp)
    
    return app