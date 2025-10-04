import uvicorn
from fastapi import FastAPI
from apis import usuario, estudiante, auditoria  # importa tus routers

app = FastAPI(title="API Proyecto Estructura de Datos")

# incluir routers
app.include_router(usuario.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(estudiante.router, prefix="/estudiantes", tags=["Estudiantes"])
app.include_router(auditoria.router, prefix="/auditorias", tags=["Auditorias"])

if __name__ == "__main__":
    uvicorn.run("menu_prueba:app", host="127.0.0.1", port=8000, reload=True)
