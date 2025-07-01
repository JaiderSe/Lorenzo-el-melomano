# Lorenzo-el-melomano

## Descripción

**Lorenzo-el-melomano** surge de la necesidad de Lorenzo, un apasionado coleccionista de música, de organizar y acceder fácilmente a su vasta colección de álbumes en diferentes formatos (discos, casetes y CDs). Para resolver sus dificultades al buscar canciones específicas, Lorenzo decide crear un sistema que almacene y gestione la información de su colección. Inspirado por la utilidad de su solución, la convierte en una aplicación web que permite a cualquier melómano registrarse, administrar sus álbumes y canciones, y editar o eliminar información según sea necesario. Cada usuario puede guardar detalles como título, año, descripción, artistas, canciones y formato de cada álbum, facilitando así la gestión y consulta de su colección musical de manera sencilla e intuitiva.


**Lorenzo-el-melomano** es una aplicación desarrollada para los amantes de la música, permitiendo explorar, organizar y compartir colecciones musicales de manera sencilla e intuitiva.

## Estructura del Proyecto



```
coleccion_musical/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── db_connection.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   ├── album.py
│   │   ├── artista.py
│   │   └── cancion.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── auth_controller.py
│   │   ├── album_controller.py
│   │   ├── artista_controller.py
│   │   └── cancion_controller.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── albums/
│   │   │   ├── list.html
│   │   │   ├── detail.html
│   │   │   ├── create.html
│   │   │   └── edit.html
│   │   ├── artistas/
│   │   │   ├── list.html
│   │   │   └── detail.html
│   │   └── canciones/
│   │       ├── list.html
│   │       ├── create.html
│   │       └── edit.html
│   └── utils/
│       ├── __init__.py
│       ├── decorators.py
│       └── helpers.py
│
├── requirements.txt
├── run.py
└── README.md
```



## Integrantes

- Jaider Moreno - Desarrollador Backend
- Juliana Tique - Desarrolladora Frontend
- David Solano - Diseñador UI/UX
- Isaura - Tester

## Tecnologías Usadas

- **Frontend:** Bootstrap, HTML5, CSS3
- **Backend:** Flask, Python
- **Base de datos:** MYSQL
- **Control de versiones:** Git & GitHub

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/Lorenzo-el-melomano.git
    ```
2. Instala las dependencias:
    ```bash
    cd Lorenzo-el-melomano
    npm install
    ```
3. Inicia la aplicación:
    ```bash
    npm start




    ```

## Licencia

Este proyecto es de uso libre.