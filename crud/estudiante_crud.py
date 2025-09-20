
from sqlalchemy.orm import Session
from models.estudiante import Estudiante
import uuid
from typing import List, Optional


def create_estudiante(db: Session, matricula: str, persona_id: uuid.UUID) -> Estudiante:
    """
    Crea un nuevo estudiante en la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        matricula (str): Número de matrícula del estudiante.
        persona_id (uuid.UUID): ID de la persona asociada al estudiante.

    Returns:
        Estudiante: Objeto del estudiante recién creado.
    """
    estudiante = Estudiante(id_estudiante=persona_id, matricula=matricula)
    db.add(estudiante)
    db.commit()
    db.refresh(estudiante)
    return estudiante


def get_estudiante_by_id(db: Session, estudiante_id: uuid.UUID) -> Optional[Estudiante]:
    """
    Obtiene un estudiante por su ID.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        estudiante_id (uuid.UUID): ID único del estudiante.

    Returns:
        Optional[Estudiante]: El estudiante si existe, en caso contrario None.
    """
    return db.query(Estudiante).filter(Estudiante.id_estudiante == estudiante_id).first()


def get_all_estudiantes(db: Session) -> List[Estudiante]:
    """
    Obtiene todos los estudiantes registrados.

    Args:
        db (Session): Sesión activa de SQLAlchemy.

    Returns:
        List[Estudiante]: Lista de todos los estudiantes.
    """
    return db.query(Estudiante).all()


def update_estudiante(db: Session, estudiante_id: uuid.UUID, matricula: Optional[str] = None) -> Optional[Estudiante]:
    """
    Actualiza los datos de un estudiante existente.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        estudiante_id (uuid.UUID): ID único del estudiante.
        matricula (Optional[str], optional): Nueva matrícula si se desea actualizar.

    Returns:
        Optional[Estudiante]: El estudiante actualizado o None si no existe.
    """
    estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == estudiante_id).first()
    if estudiante is None:
        return None

    if matricula is not None:
        estudiante.matricula = matricula

    db.commit()
    db.refresh(estudiante)
    return estudiante


def delete_estudiante(db: Session, estudiante_id: uuid.UUID) -> bool:
    """
    Elimina un estudiante de la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        estudiante_id (uuid.UUID): ID único del estudiante.

    Returns:
        bool: True si se eliminó exitosamente, False si no existe.
    """
    estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == estudiante_id).first()
    if estudiante is None:
        return False

    db.delete(estudiante)
    db.commit()
    return True
