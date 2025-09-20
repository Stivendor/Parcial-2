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
        default=uuid.uuid4
    )
    especialidad = Column(String(50), nullable=False)

    persona = relationship("Persona", backref="profesor", uselist=False)

    def __repr__(self):
        return f"<Profesor(id_profesor={self.id_profesor}, especialidad='{self.especialidad}')>"
