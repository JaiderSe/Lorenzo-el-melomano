from MySQLdb.cursors import DictCursor
# app/models/album.py
from app.database.db_connection import get_db_connection

class Album:
    @staticmethod
    def create(id_usuario, titulo, ano_produccion, descripcion, medio):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO albums (id_usuario, titulo, ano_produccion, descripcion, medio) VALUES (%s, %s, %s, %s, %s)",
            (id_usuario, titulo, ano_produccion, descripcion, medio)
        )
        album_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return album_id

    @staticmethod
    def get_by_id(album_id):
        conn = get_db_connection()
        cursor = conn.cursor(DictCursor)
        cursor.execute("SELECT * FROM albums WHERE id_album = %s", (album_id,))
        album = cursor.fetchone()
        conn.close()
        return album

    @staticmethod
    def get_all_by_user(id_usuario):
        conn = get_db_connection()
        cursor = conn.cursor(DictCursor)
        cursor.execute("""
            SELECT a.*, GROUP_CONCAT(ar.nombre_artista SEPARATOR ', ') AS artistas
            FROM albums a
            LEFT JOIN album_artistas aa ON a.id_album = aa.id_album
            LEFT JOIN artistas ar ON aa.id_artista = ar.id_artista
            WHERE a.id_usuario = %s
            GROUP BY a.id_album
            ORDER BY a.titulo
        """, (id_usuario,))
        albums = cursor.fetchall()
        conn.close()
        return albums

    @staticmethod
    def update(album_id, titulo, ano_produccion, descripcion, medio):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE albums SET titulo = %s, ano_produccion = %s, descripcion = %s, medio = %s WHERE id_album = %s",
            (titulo, ano_produccion, descripcion, medio, album_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(album_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM albums WHERE id_album = %s", (album_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def add_artist(album_id, artista_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO album_artistas (id_album, id_artista) VALUES (%s, %s)",
                (album_id, artista_id)
            )
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()

    @staticmethod
    def remove_artist(album_id, artista_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM album_artistas WHERE id_album = %s AND id_artista = %s",
            (album_id, artista_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_artists(album_id):
        conn = get_db_connection()
        cursor = conn.cursor(DictCursor)
        cursor.execute("""
            SELECT ar.id_artista, ar.nombre_artista 
            FROM album_artistas aa
            JOIN artistas ar ON aa.id_artista = ar.id_artista
            WHERE aa.id_album = %s
        """, (album_id,))
        artists = cursor.fetchall()
        conn.close()
        return artists