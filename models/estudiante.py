import uuid

from database.config import Base
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from entities.persona import Persona


class Estudiante(Persona):
    __tablename__ = "estudiantes"

    id_estudiante = Column(
        UUID(as_uuid=True),
        ForeignKey("personas.id_persona"),
        primary_key=True,
    )
    matricula = Column(String(20), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    """ Relación con Persona (uno a uno)"""
    persona = relationship("Persona", backref="estudiante", uselist=False)

    def __repr__(self):
        return f"<Estudiante(id_estudiante={self.id_estudiante}, matricula='{self.matricula}')>"

