# Proyecto de Gestión Académica

Este proyecto es un sistema de *gestión académica* desarrollado en *Python* utilizando *SQLAlchemy* como ORM y *PostgreSQL* como base de datos.  
Permite administrar *estudiantes, profesores, materias y notas* mediante un menú interactivo en consola.  
Además, incluye *auditoría* de acciones realizadas.

El proyecto está pensado para *prácticas de POO, manejo de **bases de datos relacionales* y operaciones *CRUD* (Crear, Leer, Actualizar, Eliminar).

---

## Funcionalidades

### Estudiantes
- Listar estudiantes  
- Crear estudiante  
- Actualizar estudiante (excepto ID)  
- Eliminar estudiante  

### Profesores
- Listar profesores  
- Crear profesor  
- Actualizar profesor (excepto ID)  
- Eliminar profesor  

### Materias
- Listar materias y su profesor asignado  
- Crear materia (asignando profesor)  
- Actualizar materia (excepto ID)  
- Eliminar materia  

### Notas
- Listar notas  
- Agregar nota (asignando estudiante y materia)  
- Actualizar solo el valor de la nota  

### Auditoría
- Registrar acciones realizadas en el sistema  
- Consultar historial de acciones  

---

## Tecnologías

- *Lenguaje:* Python 3.13  
- *Base de datos:* PostgreSQL  
- *ORM:* SQLAlchemy  
- *Interfaz:* Consola interactiva  
- *Herramientas:* VS Code, Black formatter  

---

## Instalación

### Clonar el repositorio
```
git clone https://github.com/Stivendor/Parcial-2.git
cd Parcial-2
```
---
## Crear un entorno virtual
```
python -m venv .venv
```
---
## Activar el entorno virtual

Windows (CMD o PowerShell):
```
.venv\Scripts\activate
```

Linux/Mac:
```
source .venv/bin/activate
```
## Instalar dependencias
```
pip install -r requirements.txt
```
## Configurar base de datos

En database/config.py, agrega tu URL de PostgreSQL:
```
DATABASE_URL = "postgresql+psycopg2://usuario:contraseña@localhost:5432/escuela_db"
```
## Ejecutar el sistema
```
python main.py
```

Sigue el menú interactivo para gestionar estudiantes, profesores, materias y notas.
```
Nota: Los IDs no se pueden actualizar, solo los demás campos.
```
## Estructura del Proyecto
```
Proyecto/ 
│── main.py              # Archivo principal con menú
│── database/
│   ├── config.py        # Configuración de base de datos
│   └── ...
│── models/              # Definición de tablas
│── crud/                # Funciones CRUD
│── requirements.txt     # Dependencias del proyecto
└── .vscode/
    └── settings.json    # Configuración de Black formatter
```
## Formateo de Código

El proyecto utiliza Black para mantener un formato uniforme.
Con .vscode/settings.json configurado:
```
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true
}
```

Cada vez que guardes un archivo .py, se formateará automáticamente.

## Autores

Julián Bermeo Cuellar

Stiven Atehortua Ochoa

Ángel Gutiérrez Ladino

ITM – Medellín, Colombia
Estudiantes de Ingeniería

