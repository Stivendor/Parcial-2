
import uuid
from sqlalchemy.orm import Session
from models.materia import Materia
from models.auditoria import Auditoria

def create_materia(db: Session, nombre: str, codigo: str, creditos: int):
    materia = Materia(
        id_materia=uuid.uuid4(),
        nombre=nombre,
        codigo=codigo,
        creditos=creditos
    )
    db.add(materia)
    db.commit()
    db.refresh(materia)
    return materia

def listar_materias(db: Session):
    materias = db.query(Materia).all()
    for m in materias:
        print(f"{m.id_materia} - {m.nombre} - {m.codigo} - {m.creditos} créditos")

def actualizar_materia(db: Session, materia_id: uuid.UUID, usuario_id: uuid.UUID):
    materia = db.query(Materia).filter(Materia.id_materia == materia_id).first()
    if not materia:
        print("Materia no encontrada")
        return

    materia.nombre = input(f"Nombre ({materia.nombre}): ") or materia.nombre
    materia.codigo = input(f"Código ({materia.codigo}): ") or materia.codigo
    creditos = input(f"Créditos ({materia.creditos}): ")
    if creditos.strip():
        materia.creditos = int(creditos)

    db.add(materia)
    auditoria = Auditoria(usuario_id=usuario_id, accion=f"Actualizó materia {materia.nombre}", tabla="materias")
    db.add(auditoria)
    db.commit()
    print(f"Materia {materia.nombre} actualizada")

def eliminar_materia(db: Session, materia_id: uuid.UUID, usuario_id: uuid.UUID):
    materia = db.query(Materia).filter(Materia.id_materia == materia_id).first()
    if not materia:
        print("Materia no encontrada")
        return

    db.delete(materia)
    auditoria = Auditoria(usuario_id=usuario_id, accion=f"Eliminó materia {materia.nombre}", tabla="materias")
    db.add(auditoria)
    db.commit()
    print(f"Materia {materia.nombre} eliminada")

