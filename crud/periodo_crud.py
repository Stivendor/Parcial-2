# crud_periodo.py
from sqlalchemy.orm import Session
from models.periodo import Periodo
import uuid
from typing import List, Optional
from datetime import date


def create_periodo(db: Session, nombre: str, fecha_inicio: date, fecha_fin: date) -> Periodo:
    """
    Crea un nuevo periodo en la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        nombre (str): Nombre del periodo académico.
        fecha_inicio (date): Fecha de inicio.
        fecha_fin (date): Fecha de finalización.

    Returns:
        Periodo: Objeto del periodo recién creado.
    """
    periodo = Periodo(nombre=nombre, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
    db.add(periodo)
    db.commit()
    db.refresh(periodo)
    return periodo


def get_periodo_by_id(db: Session, periodo_id: uuid.UUID) -> Optional[Periodo]:
    """
    Obtiene un periodo por su ID.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        periodo_id (uuid.UUID): ID único del periodo.

    Returns:
        Optional[Periodo]: El periodo si existe, en caso contrario None.
    """
    return db.query(Periodo).filter(Periodo.id_periodo == periodo_id).first()


def get_all_periodos(db: Session) -> List[Periodo]:
    """
    Obtiene todos los periodos registrados.

    Args:
        db (Session): Sesión activa de SQLAlchemy.

    Returns:
        List[Periodo]: Lista de todos los periodos.
    """
    return db.query(Periodo).all()


def update_periodo(db: Session, periodo_id: uuid.UUID, nombre: Optional[str] = None, fecha_inicio: Optional[date] = None, fecha_fin: Optional[date] = None) -> Optional[Periodo]:
    """
    Actualiza los datos de un periodo existente.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        periodo_id (uuid.UUID): ID único del periodo.
        nombre (Optional[str]): Nuevo nombre del periodo.
        fecha_inicio (Optional[date]): Nueva fecha de inicio.
        fecha_fin (Optional[date]): Nueva fecha de finalización.

    Returns:
        Optional[Periodo]: El periodo actualizado o None si no existe.
    """
    periodo = db.query(Periodo).filter(Periodo.id_periodo == periodo_id).first()
    if periodo is None:
        return None

    if nombre is not None:
        periodo.nombre = nombre
    if fecha_inicio is not None:
        periodo.fecha_inicio = fecha_inicio
    if fecha_fin is not None:
        periodo.fecha_fin = fecha_fin

    db.commit()
    db.refresh(periodo)
    return periodo


def delete_periodo(db: Session, periodo_id: uuid.UUID) -> bool:
    """
    Elimina un periodo de la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        periodo_id (uuid.UUID): ID único del periodo.

    Returns:
        bool: True si se eliminó exitosamente, False si no existe.
    """
    periodo = db.query(Periodo).filter(Periodo.id_periodo == periodo_id).first()
    if periodo is None:
        return False

    db.delete(periodo)
    db.commit()
    return True
