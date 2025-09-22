################## profesor_crud #######################
import uuid
from sqlalchemy.orm import Session
from models.persona import Persona
from models.profesor import Profesor

def create_profesor(db: Session, nombre: str, email: str, telefono: str, especialidad: str):

    nueva_persona = Persona(
        id_persona=uuid.uuid4(),
        nombre=nombre,
        email=email,
        telefono=telefono
    )
    db.add(nueva_persona)
    db.commit()
    db.refresh(nueva_persona)

    profesor = Profesor(
        id_profesor=uuid.uuid4(),
        persona_id=nueva_persona.id_persona,
        especialidad=especialidad
    )
    db.add(profesor)
    db.commit()
    db.refresh(profesor)

    return profesor

def listar_profesores(db: Session):
    return db.query(Profesor).all()

def actualizar_profesor(db: Session, profesor_id: uuid.UUID, especialidad: str = None):
    profesor = db.query(Profesor).filter(Profesor.id_profesor == profesor_id).first()
    if profesor:
        if especialidad:
            profesor.especialidad = especialidad
        db.commit()
        db.refresh(profesor)
    return profesor

def eliminar_profesor(db: Session, profesor_id: uuid.UUID):
    profesor = db.query(Profesor).filter(Profesor.id_profesor == profesor_id).first()
    if profesor:
        db.delete(profesor)
        db.commit()
    return profesor

