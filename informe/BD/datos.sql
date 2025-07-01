USE coleccion_musical;

-- Insertar usuarios
INSERT INTO usuarios (nombre, contrasena) VALUES
('Carlos Mendoza', '1234abcd'),
('Laura Pérez', 'laura2024'),
('Andrés Gómez', 'andrespass'),
('Valentina Ruiz', 'vale123'),
('Mateo Torres', 'torresmateo'),
('Camila Díaz', 'camid2024'),
('Santiago Romero', 'santi321'),
('Mariana Silva', 'mari!234'),
('David Ortega', 'david2024'),
('Isabella Herrera', 'isapass');

-- Insertar artistas
INSERT INTO artistas (nombre_artista) VALUES
('Coldplay'),
('Shakira'),
('The Beatles'),
('Juanes'),
('Adele'),
('Metallica'),
('Karol G'),
('Bad Bunny'),
('Taylor Swift'),
('Queen');

-- Insertar álbumes
INSERT INTO albums (id_usuario, titulo, ano_produccion, descripcion, medio) VALUES
(1, 'Parachutes', 2000, 'Álbum debut de Coldplay', 'CD'),
(2, 'Laundry Service', 2001, 'Álbum internacional de Shakira', 'CD'),
(3, 'Abbey Road', 1969, 'Uno de los álbumes más icónicos de The Beatles', 'Vinilo'),
(4, 'Un Día Normal', 2002, 'Uno de los más famosos de Juanes', 'CD'),
(5, '21', 2011, 'Álbum de éxito de Adele', 'CD'),
(6, 'Master of Puppets', 1986, 'Metal clásico', 'Vinilo'),
(7, 'Mañana Será Bonito', 2023, 'Pop urbano de Karol G', 'Digital'),
(8, 'YHLQMDLG', 2020, 'Bad Bunny en su mejor momento', 'Digital'),
(9, '1989', 2014, 'Pop de Taylor Swift', 'CD'),
(10, 'A Night at the Opera', 1975, 'Contiene "Bohemian Rhapsody"', 'Vinilo');

-- Insertar relación usuario-album
INSERT INTO usuario_album (id_usuario, id_album) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

-- Relación album-artistas
INSERT INTO album_artistas (id_album, id_artista) VALUES
(1, 1),  -- Coldplay - Parachutes
(2, 2),  -- Shakira - Laundry Service
(3, 3),  -- The Beatles - Abbey Road
(4, 4),  -- Juanes - Un Día Normal
(5, 5),  -- Adele - 21
(6, 6),  -- Metallica - Master of Puppets
(7, 7),  -- Karol G - MSB
(8, 8),  -- Bad Bunny - YHLQMDLG
(9, 9),  -- Taylor Swift - 1989
(10, 10);-- Queen - A Night at the Opera

-- Insertar canciones
INSERT INTO canciones (id_album, titulo_cancion, duracion, interprete) VALUES
(1, 'Yellow', 270, 'Coldplay'),
(1, 'Trouble', 260, 'Coldplay'),
(2, 'Whenever, Wherever', 215, 'Shakira'),
(2, 'Underneath Your Clothes', 220, 'Shakira'),
(3, 'Come Together', 259, 'The Beatles'),
(3, 'Something', 182, 'The Beatles'),
(4, 'A Dios le Pido', 190, 'Juanes'),
(4, 'Es Por Ti', 210, 'Juanes'),
(5, 'Rolling in the Deep', 228, 'Adele'),
(5, 'Someone Like You', 285, 'Adele'),
(6, 'Battery', 312, 'Metallica'),
(6, 'Master of Puppets', 515, 'Metallica'),
(7, 'Provenza', 240, 'Karol G'),
(7, 'TQG', 210, 'Karol G'),
(8, 'Safaera', 300, 'Bad Bunny'),
(8, 'La Difícil', 200, 'Bad Bunny'),
(9, 'Shake It Off', 242, 'Taylor Swift'),
(9, 'Blank Space', 231, 'Taylor Swift'),
(10, 'Bohemian Rhapsody', 355, 'Queen'),
(10, 'Love of My Life', 220, 'Queen');

