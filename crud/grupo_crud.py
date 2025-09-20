# crud_grupo.py
from sqlalchemy.orm import Session
from models.grupo import Grupo
import uuid
from typing import List, Optional


def create_grupo(db: Session, nombre: str, materia_id: uuid.UUID, profesor_id: uuid.UUID, periodo_id: uuid.UUID) -> Grupo:
    """
    Crea un nuevo grupo en la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        nombre (str): Nombre del grupo.
        materia_id (uuid.UUID): ID de la materia asociada.
        profesor_id (uuid.UUID): ID del profesor asociado.
        periodo_id (uuid.UUID): ID del periodo asociado.

    Returns:
        Grupo: Objeto del grupo recién creado.
    """
    grupo = Grupo(nombre=nombre, materia_id=materia_id, profesor_id=profesor_id, periodo_id=periodo_id)
    db.add(grupo)
    db.commit()
    db.refresh(grupo)
    return grupo


def get_grupo_by_id(db: Session, grupo_id: uuid.UUID) -> Optional[Grupo]:
    """
    Obtiene un grupo por su ID.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        grupo_id (uuid.UUID): ID único del grupo.

    Returns:
        Optional[Grupo]: El grupo si existe, en caso contrario None.
    """
    return db.query(Grupo).filter(Grupo.id_grupo == grupo_id).first()


def get_all_grupos(db: Session) -> List[Grupo]:
    """
    Obtiene todos los grupos registrados.

    Args:
        db (Session): Sesión activa de SQLAlchemy.

    Returns:
        List[Grupo]: Lista de todos los grupos.
    """
    return db.query(Grupo).all()


def update_grupo(db: Session, grupo_id: uuid.UUID, nombre: Optional[str] = None) -> Optional[Grupo]:
    """
    Actualiza los datos de un grupo existente.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        grupo_id (uuid.UUID): ID único del grupo.
        nombre (Optional[str], optional): Nuevo nombre del grupo.

    Returns:
        Optional[Grupo]: El grupo actualizado o None si no existe.
    """
    grupo = db.query(Grupo).filter(Grupo.id_grupo == grupo_id).first()
    if grupo is None:
        return None

    if nombre is not None:
        grupo.nombre = nombre

    db.commit()
    db.refresh(grupo)
    return grupo


def delete_grupo(db: Session, grupo_id: uuid.UUID) -> bool:
    """
    Elimina un grupo de la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        grupo_id (uuid.UUID): ID único del grupo.

    Returns:
        bool: True si se eliminó exitosamente, False si no existe.
    """
    grupo = db.query(Grupo).filter(Grupo.id_grupo == grupo_id).first()
    if grupo is None:
        return False

    db.delete(grupo)
    db.commit()
    return True
