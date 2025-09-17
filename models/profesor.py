import uuid

from database.config import Base
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.persona import Persona


class Profesor(Persona):
    __tablename__ = "profesores"

    id_profesor = Column(
        UUID(as_uuid=True),
        ForeignKey("personas.id_persona"),
        primary_key=True,
    )
    especialidad = Column(String(50), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    """ Relación con Persona (uno a uno)"""
    persona = relationship("Persona", backref="profesor", uselist=False)

    def __repr__(self):
        return f"<Profesor(id_profesor={self.id_profesor}, especialidad='{self.especialidad}')>"
