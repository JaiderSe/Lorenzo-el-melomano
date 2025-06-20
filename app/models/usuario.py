from app.database.db_connection import get_db_connection

class Usuario:
    @staticmethod
    def create(nombre, contrasena):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, contrasena) VALUES (%s, %s)",
            (nombre, contrasena)
        )
        conn.commit()
        return cursor.lastrowid
    
    @staticmethod
    def get_by_id(id_usuario):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        return cursor.fetchone()
    
    @staticmethod
    def get_by_nombre(nombre):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre = %s", (nombre,))
        return cursor.fetchone()
    
    @staticmethod
    def update(id_usuario, nombre=None, contrasena=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        if nombre and contrasena:
            cursor.execute(
                "UPDATE usuarios SET nombre = %s, contrasena = %s WHERE id_usuario = %s",
                (nombre, contrasena, id_usuario))
        elif nombre:
            cursor.execute(
                "UPDATE usuarios SET nombre = %s WHERE id_usuario = %s",
                (nombre, id_usuario))
        elif contrasena:
            cursor.execute(
                "UPDATE usuarios SET contrasena = %s WHERE id_usuario = %s",
                (contrasena, id_usuario))
        conn.commit()
    
    @staticmethod
    def delete(id_usuario):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        conn.commit()