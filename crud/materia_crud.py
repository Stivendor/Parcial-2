# crud_materia.py
from sqlalchemy.orm import Session
from models.materia import Materia
import uuid
from typing import List, Optional


def create_materia(db: Session, nombre: str, codigo: str, profesor_id: Optional[uuid.UUID] = None) -> Materia:
    """
    Crea una nueva materia en la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        nombre (str): Nombre de la materia.
        codigo (str): Código único de la materia.
        profesor_id (Optional[uuid.UUID]): ID del profesor asociado (opcional).

    Returns:
        Materia: Objeto de la materia recién creada.
    """
    materia = Materia(nombre=nombre, codigo=codigo, profesor_id=profesor_id)
    db.add(materia)
    db.commit()
    db.refresh(materia)
    return materia


def get_materia_by_id(db: Session, materia_id: uuid.UUID) -> Optional[Materia]:
    """
    Obtiene una materia por su ID.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        materia_id (uuid.UUID): ID único de la materia.

    Returns:
        Optional[Materia]: La materia si existe, en caso contrario None.
    """
    return db.query(Materia).filter(Materia.id_materia == materia_id).first()


def get_all_materias(db: Session) -> List[Materia]:
    """
    Obtiene todas las materias registradas.

    Args:
        db (Session): Sesión activa de SQLAlchemy.

    Returns:
        List[Materia]: Lista de todas las materias.
    """
    return db.query(Materia).all()


def update_materia(db: Session, materia_id: uuid.UUID, nombre: Optional[str] = None, codigo: Optional[str] = None) -> Optional[Materia]:
    """
    Actualiza los datos de una materia existente.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        materia_id (uuid.UUID): ID único de la materia.
        nombre (Optional[str]): Nuevo nombre de la materia.
        codigo (Optional[str]): Nuevo código de la materia.

    Returns:
        Optional[Materia]: La materia actualizada o None si no existe.
    """
    materia = db.query(Materia).filter(Materia.id_materia == materia_id).first()
    if materia is None:
        return None

    if nombre is not None:
        materia.nombre = nombre
    if codigo is not None:
        materia.codigo = codigo

    db.commit()
    db.refresh(materia)
    return materia


def delete_materia(db: Session, materia_id: uuid.UUID) -> bool:
    """
    Elimina una materia de la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        materia_id (uuid.UUID): ID único de la materia.

    Returns:
        bool: True si se eliminó exitosamente, False si no existe.
    """
    materia = db.query(Materia).filter(Materia.id_materia == materia_id).first()
    if materia is None:
        return False

    db.delete(materia)
    db.commit()
    return True
