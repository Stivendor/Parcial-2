import uuid
from database.config import SessionLocal
from sqlalchemy.orm import Session
from models.auditoria import Auditoria
from crud.usuario_crud import autenticar_usuario
from crud.estudiante_crud import create_estudiante, listar_estudiantes, actualizar_estudiante, eliminar_estudiante
from crud.profesor_crud import create_profesor, listar_profesores, actualizar_profesor, eliminar_profesor
from crud.materia_crud import create_materia, listar_materias, actualizar_materia, eliminar_materia
from crud.nota_crud import create_nota, get_all_notas, update_nota, delete_nota
from crud.auditoria_crud import ver_auditoria
from crud.usuario_crud import autenticar_usuario

# ==================== MENÚS ====================

def menu_estudiantes(usuario):
    db = SessionLocal()
    while True:
        print("\n=== ESTUDIANTES ===")
        print("1. Listar estudiantes")
        print("2. Crear estudiante")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("0. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            listar_estudiantes(db)
        elif opcion == "2":
            nombre = input("Nombre: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            carrera = input("Carrera: ")
            semestre = int(input("Semestre: "))
            create_estudiante(db, nombre, email, telefono, carrera, semestre, usuario.id_usuario)
        elif opcion == "3":
            estudiante_id = input("ID del estudiante: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_email = input("Nuevo email: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            nueva_carrera = input("Nueva carrera: ")
            nuevo_semestre = int(input("Nuevo semestre: "))
            actualizar_estudiante(db, estudiante_id, nuevo_nombre, nuevo_email, nuevo_telefono, nueva_carrera, nuevo_semestre, usuario.id_usuario)
        elif opcion == "4":
            estudiante_id = input("ID del estudiante: ")
            eliminar_estudiante(db, estudiante_id, usuario.id_usuario)
        elif opcion == "0":
            break
    db.close()


def menu_profesores(usuario):
    db = SessionLocal()
    while True:
        print("\n=== PROFESORES ===")
        print("1. Listar profesores")
        print("2. Crear profesor")
        print("3. Actualizar profesor")
        print("4. Eliminar profesor")
        print("0. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            listar_profesores(db)
        elif opcion == "2":
            nombre = input("Nombre: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            departamento = input("Departamento: ")
            create_profesor(db, nombre, email, telefono, departamento)
        elif opcion == "3":
            profesor_id = input("ID del profesor: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_email = input("Nuevo email: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            nuevo_departamento = input("Nuevo departamento: ")
            actualizar_profesor(db, profesor_id, nuevo_nombre, nuevo_email, nuevo_telefono, nuevo_departamento, usuario.id_usuario)
        elif opcion == "4":
            profesor_id = input("ID del profesor: ")
            eliminar_profesor(db, profesor_id, usuario.id_usuario)
        elif opcion == "0":
            break
    db.close()


def menu_materias(usuario, db):
    while True:
        print("\n=== Gestión de Materias ===")
        print("1. Crear materia")
        print("2. Listar materias")
        print("3. Actualizar materia")
        print("4. Eliminar materia")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            codigo = input("Código: ")
            creditos = input("Créditos: ")

            materia = create_materia(db, nombre, codigo, creditos)
            auditoria = Auditoria(
                usuario_id=usuario.id_usuario,
                accion=f"Creó materia {materia.nombre}",
                tabla="materias"
            )
            db.add(auditoria)
            db.commit()
            print(f"Materia {materia.nombre} creada")

        elif opcion == "2":
            listar_materias(db)

        elif opcion == "3":
            listar_materias(db)
            materia_id = input("ID de la materia a actualizar: ")
            actualizar_materia(db, uuid.UUID(materia_id), usuario.id_usuario)

        elif opcion == "4":
            listar_materias(db)
            materia_id = input("ID de la materia a eliminar: ")
            eliminar_materia(db, uuid.UUID(materia_id), usuario.id_usuario)

        elif opcion == "0":
            break
        else:
            print("Opción inválida")

def menu_notas(usuario, db):
    while True:
        print("\n=== NOTAS ===")
        print("1. Listar notas")
        print("2. Crear nota")
        print("3. Actualizar nota")
        print("4. Eliminar nota")
        print("0. Volver")

        opcion = input("Opción: ")

        if opcion == "1":
            notas = get_all_notas(db)
            for nota in notas:
                print(f"ID: {nota.id_nota}, Estudiante: {nota.estudiante_id}, Materia: {nota.materia_id}, Valor: {nota.valor}")

        elif opcion == "2":
            estudiante_id = input("ID del estudiante: ")
            materia_id = input("ID de la materia: ")
            valor = float(input("Nota: ")) 

            nueva_nota = create_nota(db, estudiante_id, materia_id, valor)
            print(f"Nota creada: {nueva_nota}")

        elif opcion == "3":
            nota_id = input("ID de la nota a actualizar: ")
            nuevo_valor = float(input("Nuevo valor de la nota: "))  

            update_nota(db, nota_id, nuevo_valor)
            print("Nota actualizada correctamente")

        elif opcion == "4":
            nota_id = input("ID de la nota a eliminar: ")
            delete_nota(db, nota_id)
            print("Nota eliminada correctamente")

        elif opcion == "0":
            break
        else:
            print("Opción inválida")



def menu_auditoria():
    db = SessionLocal()
    print("\n=== AUDITORÍA ===")
    ver_auditoria(db)
    db.close()


# ==================== MAIN ====================

def menu_principal(usuario, db):
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestionar Estudiantes")
        print("2. Gestionar Profesores")
        print("3. Gestionar Materias")
        print("4. Gestionar Notas")
        print("5. Mostrar Auditoría")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            menu_estudiantes(usuario)
        elif opcion == "2":
            menu_profesores(usuario)
        elif opcion == "3":
            menu_materias(usuario, db)
        elif opcion == "4":
            menu_notas(usuario, db)
        elif opcion == "5":
            menu_auditoria()
        elif opcion == "0":
            print("Saliendo...")
            break

def main():
    db: Session = SessionLocal()

    username = input("Usuario: ")
    password = input("Contraseña: ")

    usuario_logeado = autenticar_usuario(db, username, password)

    if usuario_logeado:
        print(f"Bienvenido {usuario_logeado.username} (rol: {usuario_logeado.rol})")
        menu_principal(usuario_logeado, db)  
    else:
        print("Usuario o contraseña incorrectos")

if __name__ == "__main__":
    main()
