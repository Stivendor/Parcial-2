# crud_profesor.py
from sqlalchemy.orm import Session
from models.profesor import Profesor
import uuid
from typing import List, Optional


def create_profesor(db: Session, persona_id: uuid.UUID, especialidad: str) -> Profesor:
    """
    Crea un nuevo profesor en la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        persona_id (uuid.UUID): ID de la persona asociada.
        especialidad (str): Especialidad del profesor.

    Returns:
        Profesor: Objeto del profesor recién creado.
    """
    profesor = Profesor(id_profesor=persona_id, especialidad=especialidad)
    db.add(profesor)
    db.commit()
    db.refresh(profesor)
    return profesor


def get_profesor_by_id(db: Session, profesor_id: uuid.UUID) -> Optional[Profesor]:
    """
    Obtiene un profesor por su ID.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        profesor_id (uuid.UUID): ID único del profesor.

    Returns:
        Optional[Profesor]: El profesor si existe, en caso contrario None.
    """
    return db.query(Profesor).filter(Profesor.id_profesor == profesor_id).first()


def get_all_profesores(db: Session) -> List[Profesor]:
    """
    Obtiene todos los profesores registrados.

    Args:
        db (Session): Sesión activa de SQLAlchemy.

    Returns:
        List[Profesor]: Lista de todos los profesores.
    """
    return db.query(Profesor).all()


def update_profesor(db: Session, profesor_id: uuid.UUID, especialidad: Optional[str] = None) -> Optional[Profesor]:
    """
    Actualiza los datos de un profesor existente.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        profesor_id (uuid.UUID): ID único del profesor.
        especialidad (Optional[str]): Nueva especialidad del profesor.

    Returns:
        Optional[Profesor]: El profesor actualizado o None si no existe.
    """
    profesor = db.query(Profesor).filter(Profesor.id_profesor == profesor_id).first()
    if profesor is None:
        return None

    if especialidad is not None:
        profesor.especialidad = especialidad

    db.commit()
    db.refresh(profesor)
    return profesor


def delete_profesor(db: Session, profesor_id: uuid.UUID) -> bool:
    """
    Elimina un profesor de la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        profesor_id (uuid.UUID): ID único del profesor.

    Returns:
        bool: True si se eliminó exitosamente, False si no existe.
    """
    profesor = db.query(Profesor).filter(Profesor.id_profesor == profesor_id).first()
    if profesor is None:
        return False

    db.delete(profesor)
    db.commit()
    return True
