# crud_persona.py
from sqlalchemy.orm import Session
from models.persona import Persona
import uuid
from typing import List, Optional


def create_persona(db: Session, nombre: str, edad: int) -> Persona:
   
    persona = Persona(nombre=nombre, edad=edad)
    db.add(persona)
    db.commit()
    db.refresh(persona)
    return persona


def get_persona_by_id(db: Session, persona_id: uuid.UUID) -> Optional[Persona]:
    
    return db.query(Persona).filter(Persona.id_persona == persona_id).first()


def get_all_personas(db: Session) -> List[Persona]:
   
    return db.query(Persona).all()


def update_persona(db: Session, persona_id: uuid.UUID, nombre: Optional[str] = None, edad: Optional[int] = None) -> Optional[Persona]:
   
    persona = db.query(Persona).filter(Persona.id_persona == persona_id).first()
    if persona is None:
        return None

    if nombre is not None:
        persona.nombre = nombre
    if edad is not None:
        persona.edad = edad

    db.commit()
    db.refresh(persona)
    return persona


def delete_persona(db: Session, persona_id: uuid.UUID) -> bool:
  
    persona = db.query(Persona).filter(Persona.id_persona == persona_id).first()
    if persona is None:
        return False

    db.delete(persona)
    db.commit()
    return True
