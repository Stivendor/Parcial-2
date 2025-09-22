

from sqlalchemy.orm import Session
from models.nota import Nota
import uuid
from typing import List, Optional


def create_nota(db, estudiante_id, materia_id, valor):
    nueva_nota = Nota(
        estudiante_id=estudiante_id,
        materia_id=materia_id,
        valor=valor
    )
    db.add(nueva_nota)
    db.commit()
    db.refresh(nueva_nota)
    return nueva_nota


def get_nota_by_id(db: Session, nota_id: uuid.UUID) -> Optional[Nota]:
    
    return db.query(Nota).filter(Nota.id_nota == nota_id).first()


def get_all_notas(db: Session) -> List[Nota]:
    
    return db.query(Nota).all()


def update_nota(db: Session, nota_id: uuid.UUID, valor: Optional[float] = None) -> Optional[Nota]:
   
    nota = db.query(Nota).filter(Nota.id_nota == nota_id).first()
    if nota is None:
        return None

    if valor is not None:
        nota.valor = valor

    db.commit()
    db.refresh(nota)
    return nota


def delete_nota(db: Session, nota_id: uuid.UUID) -> bool:

    nota = db.query(Nota).filter(Nota.id_nota == nota_id).first()
    if nota is None:
        return False

    db.delete(nota)
    db.commit()
    return True
