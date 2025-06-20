from app.database.db_connection import get_db_connection

class Cancion:
    @staticmethod
    def create(id_album, titulo_cancion, duracion, interprete):
        """
        Crea una nueva canción en un álbum
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO canciones 
            (id_album, titulo_cancion, duracion, interprete) 
            VALUES (%s, %s, %s, %s)""",
            (id_album, titulo_cancion, duracion, interprete)
        )
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_id(id_cancion):
        """
        Obtiene una canción por su ID
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM canciones WHERE id_cancion = %s", (id_cancion,))
        return cursor.fetchone()

    @staticmethod
    def get_by_album(id_album):
        """
        Obtiene todas las canciones de un álbum
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT * FROM canciones 
            WHERE id_album = %s 
            ORDER BY titulo_cancion
        """, (id_album,))
        return cursor.fetchall()

    @staticmethod
    def search_by_title(titulo):
        """
        Busca canciones por título (búsqueda parcial)
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM canciones WHERE titulo_cancion LIKE %s",
            (f"%{titulo}%",)
        )
        return cursor.fetchall()

    @staticmethod
    def update(id_cancion, titulo_cancion=None, duracion=None, interprete=None):
        """
        Actualiza la información de una canción
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        
        updates = []
        params = []
        
        if titulo_cancion:
            updates.append("titulo_cancion = %s")
            params.append(titulo_cancion)
        if duracion:
            updates.append("duracion = %s")
            params.append(duracion)
        if interprete:
            updates.append("interprete = %s")
            params.append(interprete)
            
        params.append(id_cancion)
        
        if updates:
            query = "UPDATE canciones SET " + ", ".join(updates) + " WHERE id_cancion = %s"
            cursor.execute(query, params)
            conn.commit()

    @staticmethod
    def delete(id_cancion):
        """
        Elimina una canción
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM canciones WHERE id_cancion = %s", (id_cancion,))
        conn.commit()