
from sqlalchemy.orm import Session
from models.nota import Nota
import uuid
from typing import List, Optional


def create_nota(db: Session, valor: float, estudiante_id: uuid.UUID, materia_id: uuid.UUID) -> Nota:
    """
    Crea una nueva nota en la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        valor (float): Valor numérico de la nota.
        estudiante_id (uuid.UUID): ID del estudiante asociado.
        materia_id (uuid.UUID): ID de la materia asociada.

    Returns:
        Nota: Objeto de la nota recién creada.
    """
    nota = Nota(valor=valor, estudiante_id=estudiante_id, materia_id=materia_id)
    db.add(nota)
    db.commit()
    db.refresh(nota)
    return nota


def get_nota_by_id(db: Session, nota_id: uuid.UUID) -> Optional[Nota]:
    """
    Obtiene una nota por su ID.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        nota_id (uuid.UUID): ID único de la nota.

    Returns:
        Optional[Nota]: La nota si existe, en caso contrario None.
    """
    return db.query(Nota).filter(Nota.id_nota == nota_id).first()


def get_all_notas(db: Session) -> List[Nota]:
    """
    Obtiene todas las notas registradas.

    Args:
        db (Session): Sesión activa de SQLAlchemy.

    Returns:
        List[Nota]: Lista de todas las notas.
    """
    return db.query(Nota).all()


def update_nota(db: Session, nota_id: uuid.UUID, valor: Optional[float] = None) -> Optional[Nota]:
    """
    Actualiza el valor de una nota existente.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        nota_id (uuid.UUID): ID único de la nota.
        valor (Optional[float]): Nuevo valor de la nota.

    Returns:
        Optional[Nota]: La nota actualizada o None si no existe.
    """
    nota = db.query(Nota).filter(Nota.id_nota == nota_id).first()
    if nota is None:
        return None

    if valor is not None:
        nota.valor = valor

    db.commit()
    db.refresh(nota)
    return nota


def delete_nota(db: Session, nota_id: uuid.UUID) -> bool:
    """
    Elimina una nota de la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        nota_id (uuid.UUID): ID único de la nota.

    Returns:
        bool: True si se eliminó exitosamente, False si no existe.
    """
    nota = db.query(Nota).filter(Nota.id_nota == nota_id).first()
    if nota is None:
        return False

    db.delete(nota)
    db.commit()
    return True
