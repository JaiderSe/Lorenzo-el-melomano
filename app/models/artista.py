from app.database.db_connection import get_db_connection

class Artista:
    @staticmethod
    def create(nombre_artista):
        """
        Crea un nuevo artista
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO artistas (nombre_artista) VALUES (%s)",
            (nombre_artista,)
        )
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_id(id_artista):
        """
        Obtiene un artista por su ID
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM artistas WHERE id_artista = %s", (id_artista,))
        return cursor.fetchone()

    @staticmethod
    def get_by_name(nombre_artista):
        """
        Busca artistas por nombre (búsqueda parcial)
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM artistas WHERE nombre_artista LIKE %s",
            (f"%{nombre_artista}%",)
        )
        return cursor.fetchall()

    @staticmethod
    def get_by_album(id_album):
        """
        Obtiene todos los artistas asociados a un álbum
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT ar.* 
            FROM artistas ar
            JOIN album_artistas aa ON ar.id_artista = aa.id_artista
            WHERE aa.id_album = %s
        """, (id_album,))
        return cursor.fetchall()

    @staticmethod
    def get_all():
        """
        Obtiene todos los artistas ordenados por nombre
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM artistas ORDER BY nombre_artista")
        return cursor.fetchall()

    @staticmethod
    def update(id_artista, nombre_artista):
        """
        Actualiza el nombre de un artista
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE artistas SET nombre_artista = %s WHERE id_artista = %s",
            (nombre_artista, id_artista)
        )
        conn.commit()

    @staticmethod
    def delete(id_artista):
        """
        Elimina un artista (las relaciones en album_artistas se eliminan por CASCADE)
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM artistas WHERE id_artista = %s", (id_artista,))
        conn.commit()