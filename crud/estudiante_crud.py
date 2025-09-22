
################ estudiante_crud ######################
import uuid
from sqlalchemy.orm import Session
from models.persona import Persona
from models.estudiante import Estudiante

def create_estudiante(db: Session, nombre: str, email: str, telefono: str, carrera: str, semestre: int, usuario_id=None):
    persona = Persona(nombre=nombre, email=email, telefono=telefono)
    db.add(persona)
    db.commit()
    db.refresh(persona)

    estudiante = Estudiante(persona_id=persona.id_persona, carrera=carrera, semestre=semestre)
    db.add(estudiante)
    db.commit()
    db.refresh(estudiante)

    if usuario_id:
        from models.auditoria import Auditoria
        auditoria = Auditoria(usuario_id=usuario_id, accion="Creación de estudiante", tabla="estudiantes")
        db.add(auditoria)
        db.commit()

    return estudiante


def listar_estudiantes(db: Session):
    return db.query(Estudiante).all()

def actualizar_estudiante(db: Session, estudiante_id: uuid.UUID, carrera: str = None, semestre: int = None):
    estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == estudiante_id).first()
    if estudiante:
        if carrera:
            estudiante.carrera = carrera
        if semestre:
            estudiante.semestre = semestre
        db.commit()
        db.refresh(estudiante)
    return estudiante

def eliminar_estudiante(db: Session, estudiante_id: uuid.UUID):
    estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == estudiante_id).first()
    if estudiante:
        db.delete(estudiante)
        db.commit()
    return estudiante

