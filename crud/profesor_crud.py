import uuid
from sqlalchemy.orm import Session
from models import Auditoria
from models.profesor import Profesor
from models.persona import Persona

def create_profesor(db, nombre, email, telefono, especialidad):
    persona = Persona(
        nombre=nombre,
        email=email,
        telefono=telefono
    )
    db.add(persona)
    db.commit()
    db.refresh(persona)

    profesor = Profesor(
        id_profesor=persona.id_persona,
        especialidad=especialidad
    )
    
    db.add(profesor)
    db.commit()
    db.refresh(profesor)
    return profesor


def listar_profesores(db: Session):
    profesores = db.query(Profesor).all()
    for p in profesores:
        print(f"{p.id_profesor} - {p.persona.nombre} - {p.especialidad}")

def actualizar_profesor(db: Session, profesor_id: uuid.UUID, usuario_id: uuid.UUID):
    profesor = db.query(Profesor).get(profesor_id)
    if not profesor:
        print("Profesor no encontrado")
        return

    profesor.especialidad = input(f"Especialidad ({profesor.especialidad}): ") or profesor.especialidad
    db.add(profesor)
    auditoria = Auditoria(usuario_id=usuario_id, accion=f"Actualizó profesor {profesor.persona.nombre}", tabla="profesores")
    db.add(auditoria)
    db.commit()
    print(f"✅ Profesor {profesor.persona.nombre} actualizado")

def eliminar_profesor(db: Session, profesor_id: uuid.UUID, usuario_id: uuid.UUID):
    profesor = db.query(Profesor).get(profesor_id)
    if not profesor:
        print("Profesor no encontrado")
        return

    db.delete(profesor)
    auditoria = Auditoria(usuario_id=usuario_id, accion=f"Eliminó profesor {profesor.persona.nombre}", tabla="profesores")
    db.add(auditoria)
    db.commit()
    print(f"Profesor {profesor.persona.nombre} eliminado")
