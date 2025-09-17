from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    rol = Column(String(20), nullable=False)

    """ Un usuario puede estar asociado a un estudiante o un profesor (relación 1 a 1)"""
    estudiante_id = Column(Integer, ForeignKey("estudiantes.id"), nullable=True)
    profesor_id = Column(Integer, ForeignKey("profesores.id"), nullable=True)

    """ Relaciones"""
    estudiante = relationship("Estudiante", backref="usuario", uselist=False)
    profesor = relationship("Profesor", backref="usuario", uselist=False)

    def __repr__(self):
        return f"<Usuario(id={self.id}, username='{self.username}', rol='{self.rol}')>"
