# Biblioteca Alameda — API (Backend)

API REST del sistema de gestión bibliotecaria **Biblioteca Alameda**. Construida con **Django** y **Django REST Framework** sobre **PostgreSQL**, con autenticación por token. Expone operaciones CRUD para autores, géneros, libros, clientes, bibliotecarios y préstamos, y es consumida por un frontend SPA desarrollado en Angular.

## 🛠️ Tecnologías

- **Python** 3.11
- **Django** 5.2
- **Django REST Framework**
- **PostgreSQL** (gestionado con pgAdmin)
- **django-cors-headers** — manejo de CORS para el frontend
- **django-filter** — filtrado de querysets
- **psycopg2-binary** — conector de PostgreSQL
- **python-dotenv** — carga de variables de entorno

## ✨ Funcionalidades

- Autenticación por token (login / logout).
- CRUD de **autores**, **géneros**, **libros**, **clientes** y **bibliotecarios**.
- Gestión de **préstamos**: registro, edición, historial y activación/desactivación de libros.
- Consultas de actividad: libros más prestados y clientes más activos.
- Manejo de roles (bibliotecario / cliente).

## 📋 Requisitos previos

- Python 3.11 o superior
- PostgreSQL 16 (y pgAdmin para administrarlo visualmente)
- pip y virtualenv

## 🚀 Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/alejandroamadorlag/proyecto-bibliotecaVirtual-api.git
cd proyecto-bibliotecaVirtual-api
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv biblioteca-web
# macOS / Linux:
source biblioteca-web/bin/activate
# Windows:
biblioteca-web\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Copia el archivo de ejemplo y rellena tus valores:

```bash
cp .env.example .env
```

Luego edita `.env` con tus datos (ver sección **Variables de entorno**).

### 5. Crear la base de datos

En pgAdmin (o por terminal) crea una base de datos vacía, por ejemplo `proyecto_biblioteca_virtual_db`, con el usuario que vayas a usar en el `.env`.

### 6. Aplicar las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. (Opcional) Crear un superusuario

```bash
python manage.py createsuperuser
```

### 8. Levantar el servidor

```bash
python manage.py runserver
```

La API queda disponible en `http://127.0.0.1:8000/`.

## 🔐 Variables de entorno

El proyecto lee su configuración sensible desde un archivo `.env` (que **no** se versiona). Usa `.env.example` como plantilla:

| Variable | Descripción | Ejemplo |
|---|---|---|
| `SECRET_KEY` | Llave secreta de Django | `genera-una-con-get_random_secret_key` |
| `DEBUG` | Modo depuración (`True`/`False`) | `True` |
| `ALLOWED_HOSTS` | Hosts permitidos (separados por coma) | `127.0.0.1,localhost` |
| `DB_NAME` | Nombre de la base de datos | `proyecto_biblioteca_virtual_db` |
| `DB_USER` | Usuario de PostgreSQL | `postgres` |
| `DB_PASSWORD` | Contraseña de PostgreSQL | `tu_password` |
| `DB_HOST` | Host de la base de datos | `127.0.0.1` |
| `DB_PORT` | Puerto de PostgreSQL | `5432` |

Para generar una `SECRET_KEY` nueva:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 📡 Endpoints principales

Base URL: `http://127.0.0.1:8000/`

### Autenticación

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/token/` | Iniciar sesión (devuelve el token) |
| POST | `/logout/` | Cerrar sesión |

### Autores

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/autores/` | Registrar autor |
| GET | `/lista-autores/` | Listar autores |
| PUT | `/delete-autor/?id={id}` | Eliminar autor (baja lógica) |

### Géneros

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/generos/` | Registrar género |
| GET | `/lista-generos/` | Listar géneros |
| PUT | `/delete-genero/?id={id}` | Eliminar género (baja lógica) |

### Libros

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/libros/` | Registrar libro |
| GET | `/lista-libros/` | Listar libros disponibles |
| GET | `/lista-librosno/` | Listar libros no disponibles |
| GET | `/lista-librospo/` | Listar libros más prestados |
| PUT | `/delete-libro/?id_libro={id}` | Eliminar libro (baja lógica) |

### Clientes

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/clientes/` | Registrar cliente |
| GET | `/lista-clientes/` | Listar clientes |
| GET | `/lista-clientesmas/` | Listar clientes más activos |
| PUT | `/delete-cliente/?id={id}` | Eliminar cliente (baja lógica) |

### Bibliotecarios / Usuarios

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/bibliotecarios/` | Registrar bibliotecario |
| GET | `/lista-bibliotecarios/` | Listar bibliotecarios |
| GET | `/lista-users/` | Listar usuarios |
| PUT | `/delete-user/?id={id}` | Eliminar usuario (baja lógica) |

### Préstamos

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/prestamos/` | Registrar préstamo |
| GET | `/lista-prestamos/` | Listar préstamos |
| GET | `/lista-prestamos-cliente/` | Listar préstamos por cliente |
| GET | `/historial/` | Historial de préstamos |
| PUT | `/prestamos-edit/` | Editar préstamo |
| PUT | `/libro-inactivo/` | Marcar libro como no disponible |
| PUT | `/libro-activo/` | Marcar libro como disponible |
| PUT | `/cliente-prestamos/` | Incrementar préstamos del cliente |

> La mayoría de los endpoints requieren el token en el header:
> `Authorization: Bearer {token}`

## 📁 Estructura del proyecto

```
proyecto-bibliotecaVirtual-api/
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── proyecto_bibliotecaVirtual_api/
    ├── settings.py          # Configuración (lee variables del .env)
    ├── urls.py              # Rutas de la API
    ├── models.py            # Modelos de datos
    ├── serializers.py       # Serializadores de DRF
    ├── views/               # Vistas por entidad
    │   ├── auth.py
    │   ├── autores.py
    │   ├── generos.py
    │   ├── libros.py
    │   ├── clientes.py
    │   ├── users.py
    │   └── prestamos.py
    ├── file_storage/        # Almacenamiento de archivos
    └── migrations/          # Migraciones de la base de datos
```

## 🔗 Frontend

Este backend es consumido por el frontend del proyecto, desarrollado en **Angular 22**:
_(agrega aquí el enlace a tu repositorio del frontend)_

## 👤 Autor

**Alejandro Amador Lagunes**
