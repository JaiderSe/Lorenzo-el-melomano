from app.database.db_connection import get_db_connection

class Album:
    @staticmethod
    def create(id_usuario, titulo, ano_produccion, descripcion, medio):
        """
        Crea un nuevo álbum en la base de datos
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO albums 
            (id_usuario, titulo, ano_produccion, descripcion, medio) 
            VALUES (%s, %s, %s, %s, %s)""",
            (id_usuario, titulo, ano_produccion, descripcion, medio)
        )
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_id(id_album):
        """
        Obtiene un álbum por su ID
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM albums WHERE id_album = %s", (id_album,))
        return cursor.fetchone()

    @staticmethod
    def get_by_user(id_usuario):
        """
        Obtiene todos los álbumes de un usuario
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT a.*, GROUP_CONCAT(ar.nombre_artista SEPARATOR ', ') as artistas
            FROM albums a
            LEFT JOIN album_artistas aa ON a.id_album = aa.id_album
            LEFT JOIN artistas ar ON aa.id_artista = ar.id_artista
            WHERE a.id_usuario = %s
            GROUP BY a.id_album
            ORDER BY a.titulo
        """, (id_usuario,))
        return cursor.fetchall()

    @staticmethod
    def update(id_album, titulo, ano_produccion, descripcion, medio):
        """
        Actualiza la información de un álbum
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE albums 
            SET titulo = %s, ano_produccion = %s, descripcion = %s, medio = %s 
            WHERE id_album = %s""",
            (titulo, ano_produccion, descripcion, medio, id_album)
        )
        conn.commit()

    @staticmethod
    def delete(id_album):
        """
        Elimina un álbum (y sus relaciones por las FOREIGN KEY con CASCADE)
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM albums WHERE id_album = %s", (id_album,))
        conn.commit()

    @staticmethod
    def add_artist(id_album, id_artista):
        """
        Añade un artista a un álbum
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO album_artistas (id_album, id_artista) VALUES (%s, %s)",
                (id_album, id_artista)
            )
            conn.commit()
            return True
        except:
            conn.rollback()
            return False

    @staticmethod
    def remove_artist(id_album, id_artista):
        """
        Elimina un artista de un álbum
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM album_artistas WHERE id_album = %s AND id_artista = %s",
            (id_album, id_artista)
        )
        conn.commit()