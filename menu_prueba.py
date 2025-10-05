import uvicorn
from fastapi import FastAPI
from apis import usuario, estudiante, auditoria, profesor, materia, nota, grupo, periodo, persona # importa tus routers

app = FastAPI(title="API Proyecto Estructura de Datos")

# incluir routers
app.include_router(usuario.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(estudiante.router, prefix="/estudiantes", tags=["Estudiantes"])
app.include_router(auditoria.router, prefix="/auditorias", tags=["Auditorias"])
app.include_router(profesor.router, prefix="/profesores", tags=["Profesores"])
app.include_router(materia.router, prefix="/materias", tags=["Materias"])
app.include_router(nota.router, prefix="/notas", tags=["Notas"])
app.include_router(grupo.router, prefix="/grupos", tags=["Grupos"])
app.include_router(periodo.router, prefix="/periodos", tags=["Periodo"])
app.include_router(persona.router, prefix="/personas", tags=["Personas"])

if __name__ == "__main__":
    uvicorn.run("menu_prueba:app", host="127.0.0.1", port=8000, reload=True)

