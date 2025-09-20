# crud_usuario.py
from sqlalchemy.orm import Session
from models.usuarios import Usuario
from typing import List, Optional


def create_usuario(db: Session, username: str, password: str, rol: str, estudiante_id: Optional[int] = None, profesor_id: Optional[int] = None) -> Usuario:
    """
    Crea un nuevo usuario en la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        username (str): Nombre de usuario único.
        password (str): Contraseña encriptada o en texto plano.
        rol (str): Rol del usuario (ejemplo: 'admin', 'profesor', 'estudiante').
        estudiante_id (Optional[int]): ID de estudiante asociado.
        profesor_id (Optional[int]): ID de profesor asociado.

    Returns:
        Usuario: Objeto del usuario recién creado.
    """
    usuario = Usuario(username=username, password=password, rol=rol, estudiante_id=estudiante_id, profesor_id=profesor_id)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def get_usuario_by_id(db: Session, usuario_id: int) -> Optional[Usuario]:
    """
    Obtiene un usuario por su ID.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        usuario_id (int): ID único del usuario.

    Returns:
        Optional[Usuario]: El usuario si existe, en caso contrario None.
    """
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def get_all_usuarios(db: Session) -> List[Usuario]:
    """
    Obtiene todos los usuarios registrados.

    Args:
        db (Session): Sesión activa de SQLAlchemy.

    Returns:
        List[Usuario]: Lista de todos los usuarios.
    """
    return db.query(Usuario).all()


def update_usuario(db: Session, usuario_id: int, username: Optional[str] = None, password: Optional[str] = None, rol: Optional[str] = None) -> Optional[Usuario]:
    """
    Actualiza los datos de un usuario existente.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        usuario_id (int): ID único del usuario.
        username (Optional[str]): Nuevo nombre de usuario.
        password (Optional[str]): Nueva contraseña.
        rol (Optional[str]): Nuevo rol.

    Returns:
        Optional[Usuario]: El usuario actualizado o None si no existe.
    """
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        return None

    if username is not None:
        usuario.username = username
    if password is not None:
        usuario.password = password
    if rol is not None:
        usuario.rol = rol

    db.commit()
    db.refresh(usuario)
    return usuario


def delete_usuario(db: Session, usuario_id: int) -> bool:
    """
    Elimina un usuario de la base de datos.

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        usuario_id (int): ID único del usuario.

    Returns:
        bool: True si se eliminó exitosamente, False si no existe.
    """
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        return False

    db.delete(usuario)
    db.commit()
    return True
