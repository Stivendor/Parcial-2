import uuid
from sqlalchemy.orm import Session
from models.persona import Persona
from models.profesor import Profesor
from sqlalchemy.orm import joinedload

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
    # Traer también la info de persona usando joinedload
    profesores = db.query(Profesor).options(joinedload(Profesor.persona)).all()
    for p in profesores:
        print(f"ID: {p.id_profesor}, Nombre: {p.persona.nombre}, Email: {p.persona.email}, Teléfono: {p.persona.telefono}, Especialidad: {p.especialidad}")
    return profesores


def actualizar_profesor(
    db: Session,
    profesor_id: uuid.UUID,
    nuevo_nombre: str = None,
    nuevo_email: str = None,
    nuevo_telefono: str = None,
    nueva_especialidad: str = None
):
    profesor = db.query(Profesor).filter(Profesor.id_profesor == profesor_id).first()
    if profesor:
        persona = db.query(Persona).filter(Persona.id_persona == profesor.persona_id).first()
        if persona:
            if nuevo_nombre:
                persona.nombre = nuevo_nombre
            if nuevo_email:
                persona.email = nuevo_email
            if nuevo_telefono:
                persona.telefono = nuevo_telefono
            db.add(persona)

        if nueva_especialidad:
            profesor.especialidad = nueva_especialidad

        db.commit()
        db.refresh(profesor)
        return profesor
    return None


def eliminar_profesor(db: Session, profesor_id: uuid.UUID):
    profesor = db.query(Profesor).filter(Profesor.id_profesor == profesor_id).first()
    if profesor:
        # Eliminar también la persona asociada
        persona = db.query(Persona).filter(Persona.id_persona == profesor.persona_id).first()
        if persona:
            db.delete(persona)
        db.delete(profesor)
        db.commit()
    return profesor
