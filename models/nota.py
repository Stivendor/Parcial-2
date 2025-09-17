import uuid

from database.config import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Nota(Base):
    __tablename__ = "notas"

    id_nota = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    valor = Column(Float, nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    """ Claves foráneas"""
    estudiante_id = Column(
        UUID(as_uuid=True), ForeignKey("estudiantes.id_estudiante"), nullable=False
    )
    materia_id = Column(
        UUID(as_uuid=True), ForeignKey("materias.id_materia"), nullable=False
    )

    """ Relaciones"""
    estudiante = relationship("Estudiante", back_populates="notas")
    materia = relationship("Materia", back_populates="notas")

    def __repr__(self):
        return f"<Nota(id_nota={self.id_nota}, valor={self.valor})>"
