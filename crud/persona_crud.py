# crud_persona.py
from sqlalchemy.orm import Session
from models.persona import Persona
import uuid
from typing import List, Optional


def create_persona(db: Session, nombre: str, edad: int) -> Persona:
    """
    Crea una nueva persona en la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        nombre (str): Nombre completo de la persona.
        edad (int): Edad de la persona.

    Returns:
        Persona: Objeto de la persona recién creada.
    """
    persona = Persona(nombre=nombre, edad=edad)
    db.add(persona)
    db.commit()
    db.refresh(persona)
    return persona


def get_persona_by_id(db: Session, persona_id: uuid.UUID) -> Optional[Persona]:
    """
    Obtiene una persona por su ID.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        persona_id (uuid.UUID): ID único de la persona.

    Returns:
        Optional[Persona]: La persona si existe, en caso contrario None.
    """
    return db.query(Persona).filter(Persona.id_persona == persona_id).first()


def get_all_personas(db: Session) -> List[Persona]:
    """
    Obtiene todas las personas registradas.

    Args:
        db (Session): Sesión activa de SQLAlchemy.

    Returns:
        List[Persona]: Lista de todas las personas.
    """
    return db.query(Persona).all()


def update_persona(db: Session, persona_id: uuid.UUID, nombre: Optional[str] = None, edad: Optional[int] = None) -> Optional[Persona]:
    """
    Actualiza los datos de una persona existente.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        persona_id (uuid.UUID): ID único de la persona.
        nombre (Optional[str]): Nuevo nombre de la persona.
        edad (Optional[int]): Nueva edad de la persona.

    Returns:
        Optional[Persona]: La persona actualizada o None si no existe.
    """
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
    """
    Elimina una persona de la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        persona_id (uuid.UUID): ID único de la persona.

    Returns:
        bool: True si se eliminó exitosamente, False si no existe.
    """
    persona = db.query(Persona).filter(Persona.id_persona == persona_id).first()
    if persona is None:
        return False

    db.delete(persona)
    db.commit()
    return True
