from models.estudiante import Estudiante
from models.persona import Persona
from models import Auditoria
from sqlalchemy.orm import Session
import uuid

def create_estudiante(db, nombre, email, telefono, carrera, semestre):
    persona = Persona(
        nombre=nombre,
        email=email,
        telefono=telefono
    )
    db.add(persona)
    db.commit()
    db.refresh(persona)
    

    estudiante = Estudiante(
        id_estudiante = persona.id_persona,
        persona_id = persona.id_persona,
        carrera=carrera,
        semestre=semestre
    )
    
    db.add(estudiante)
    db.commit()
    db.refresh(estudiante)

    return estudiante


def listar_estudiantes(db: Session):
    estudiantes = db.query(Estudiante).all()
    for e in estudiantes:
        print(f"{e.id_estudiante} - {e.persona.nombre} - {e.carrera} - {e.semestre}")

def actualizar_estudiante(db: Session, estudiante_id: uuid.UUID, usuario_id: uuid.UUID):
    estudiante = db.query(Estudiante).get(estudiante_id)
    if not estudiante:
        print("Estudiante no encontrado")
        return

    estudiante.carrera = input(f"Carrera ({estudiante.carrera}): ") or estudiante.carrera
    estudiante.semestre = input(f"Semestre ({estudiante.semestre}): ") or estudiante.semestre
    db.add(estudiante)

    auditoria = Auditoria(usuario_id=usuario_id, accion=f"Actualizó estudiante {estudiante.persona.nombre}", tabla="estudiantes")
    db.add(auditoria)

    db.commit()
    print(f" Estudiante {estudiante.persona.nombre} actualizado")

def eliminar_estudiante(db: Session, estudiante_id: uuid.UUID, usuario_id: uuid.UUID):
    estudiante = db.query(Estudiante).get(estudiante_id)
    if not estudiante:
        print("Estudiante no encontrado")
        return

    db.delete(estudiante)
    auditoria = Auditoria(usuario_id=usuario_id, accion=f"Eliminó estudiante {estudiante.persona.nombre}", tabla="estudiantes")
    db.add(auditoria)

    db.commit()
    print(f" Estudiante {estudiante.persona.nombre} eliminado")
