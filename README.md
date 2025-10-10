# Proyecto Escuela - API REST con FastAPI y PostgreSQL

Este proyecto implementa una **API REST** para la gestión de una escuela, desarrollada con **FastAPI**, **SQLAlchemy** y **PostgreSQL**, utilizando migraciones con **Alembic**.  

Permite administrar entidades como:
- Usuarios (con UUID)
- Profesores
- Estudiantes
- Grupos
- Materias
- Notas
- Períodos académicos
- Auditorías  

---

## Tecnologías principales

- [Python 3.12+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)

---

## Estructura del proyecto
```bash
PARCIAL-2/
│
├── apis/
│ ├── auditoria.py
│ ├── estudiante.py
│ ├── grupo.py
│ ├── materia.py
│ ├── nota.py
│ ├── periodo.py
│ ├── profesor.py
│ └── usuario.py
│
├── crud/
│ ├── auditoria_crud.py
│ ├── estudiante_crud.py
│ ├── grupo_crud.py
│ ├── materia_crud.py
│ ├── nota_crud.py
│ ├── periodo_crud.py
│ ├── persona_crud.py
│ ├── profesor_crud.py
│ └── usuario_crud.py
│
├── database/
│ ├── config.py
│ └── init.py
│
├── migrations/
│ ├── env.py
│ ├── schemas.py
│ ├── versions/
│ └── script.py.mako
│
├── models/
│ ├── auditoria.py
│ ├── estudiante.py
│ ├── grupo.py
│ ├── materia.py
│ ├── nota.py
│ ├── periodo.py
│ ├── persona.py
│ ├── profesor.py
│ └── usuarios.py
│
├── .gitignore.py
├── mainAPI.py
├── mainORM.py
├── requirements.txt
├── alembic.ini
├── .env # ESTE ARCHIVO SE DEBE CREAR AL CLONAR EL REPO
├── pyproject.toml
├── README.md
└── settings.json
```

---

## Configuración del entorno

### 1️. Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd PARCIAL-2
```
### 2. Crear y activar un entorno virtual
```bash
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
```
### 3. Instalar dependencias
```bash
py -m pip install -r requirements.txt
```
### Configurar variables de entorno
Crea un archivo .env en la raíz del proyecto con el siguiente contenido:

```bash
DATABASE_URL=postgresql+psycopg2://usuario:password@localhost:5432/escuela_db
```

Ejecutar el servidor

```bash
py .\mainAPI.py
```
Luego abre tu navegador en:
```bash
http://127.0.0.1:8000/docs
```
Ahí podrás explorar la documentación interactiva de la API.

## Ejemplo de endpoint - Eliminar usuario

Método: DELETE /usuarios/{usuario_id}
```bash
@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: str, db: Session = Depends(get_db)):
    """
    Elimina un usuario de la base de datos por su UUID.
    """
    eliminado = crud_usuario.delete_usuario(db, usuario_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado correctamente"}
```

Ejemplo de llamada:
```bash
DELETE /usuarios/3a0c7b6e-4e83-4208-b3f2-71a94801d33c
```

Dependencias principales
```bash
fastapi
uvicorn
sqlalchemy
alembic
psycopg2
python-dotenv
pydantic
```


# Autores

### Julián Bermeo Cuellar
### Stiven Atehortua Ochoa
### Ángel Gutiérrez Ladino

ITM – Medellín, Colombia
Estudiantes de Ingeniería
