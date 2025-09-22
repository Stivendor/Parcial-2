import uuid
from database.config import SessionLocal
from sqlalchemy.orm import Session
from models.auditoria import Auditoria
from crud.usuario_crud import autenticar_usuario
from crud.estudiante_crud import (
    create_estudiante,
    listar_estudiantes,
    actualizar_estudiante,
    eliminar_estudiante,
)
from crud.profesor_crud import (
    create_profesor,
    listar_profesores,
    actualizar_profesor,
    eliminar_profesor,
)
from crud.materia_crud import (
    create_materia,
    listar_materias,
    actualizar_materia,
    eliminar_materia,
)
from crud.nota_crud import create_nota, listar_notas, actualizar_nota, eliminar_nota
from crud.auditoria_crud import ver_auditoria


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
            estudiantes = listar_estudiantes(db)
            if not estudiantes:
                print(" No hay estudiantes registrados.")
            else:
                for est in estudiantes:
                    print(
                        f"ID: {est.id_estudiante}, Nombre: {est.persona.nombre}, Carrera: {est.carrera}, Semestre: {est.semestre}"
                    )

        elif opcion == "2":
            nombre = input("Nombre: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            carrera = input("Carrera: ")
            semestre = int(input("Semestre: "))
            create_estudiante(
                db, nombre, email, telefono, carrera, semestre, usuario.id_usuario
            )
            print("Estudiante creado correctamente.")

        elif opcion == "3":
            estudiantes = listar_estudiantes(db)
            if not estudiantes:
                print("No hay estudiantes para actualizar.")
                continue

            for est in estudiantes:
                print(
                    f"{est.id_estudiante} - {est.persona.nombre} ({est.carrera}, Sem {est.semestre})"
                )

            estudiante_id = input("\nID del estudiante a actualizar: ")
            try:
                estudiante_uuid = uuid.UUID(estudiante_id)
            except ValueError:
                print("ID inválido.")
                continue

            nuevo_nombre = input("Nuevo nombre (ENTER para no cambiar): ") or None
            nuevo_email = input("Nuevo email (ENTER para no cambiar): ") or None
            nuevo_telefono = input("Nuevo teléfono (ENTER para no cambiar): ") or None
            nueva_carrera = input("Nueva carrera (ENTER para no cambiar): ") or None
            semestre_input = input("Nuevo semestre (ENTER para no cambiar): ")
            nuevo_semestre = int(semestre_input) if semestre_input.strip() else None

            estudiante_actualizado = actualizar_estudiante(
                db,
                estudiante_uuid,
                nuevo_nombre,
                nuevo_email,
                nuevo_telefono,
                nueva_carrera,
                nuevo_semestre,
                usuario.id_usuario,
            )

            if estudiante_actualizado:
                print("Estudiante actualizado correctamente.")
            else:
                print("No se encontró estudiante con ese ID.")

        elif opcion == "4":
            estudiantes = listar_estudiantes(db)
            if not estudiantes:
                print("No hay estudiantes para eliminar.")
                continue

            for est in estudiantes:
                print(f"{est.id_estudiante} - {est.persona.nombre}")

            estudiante_id = input("ID del estudiante a eliminar: ")
            try:
                estudiante_uuid = uuid.UUID(estudiante_id)
            except ValueError:
                print("ID inválido.")
                continue

            eliminado = eliminar_estudiante(db, estudiante_uuid, usuario.id_usuario)
            if eliminado:
                print("🗑️ Estudiante eliminado correctamente.")
            else:
                print("No se encontró estudiante con ese ID.")

        elif opcion == "0":
            break
        else:
            print("Opción inválida, intente de nuevo.")
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
            especialidad = input("Especialidad: ")
            create_profesor(db, nombre, email, telefono, especialidad)
            print(" Profesor creado correctamente.")

        elif opcion == "3":
            # Listar antes para que el usuario vea los IDs
            profesores = listar_profesores(db)
            if not profesores:
                print(" No hay profesores registrados.")
                continue

            profesor_id = input("ID del profesor a actualizar: ")
            try:
                profesor_uuid = uuid.UUID(profesor_id)
            except ValueError:
                print(" ID inválido.")
                continue

            nuevo_nombre = input("Nuevo nombre (deja vacío para no cambiar): ") or None
            nuevo_email = input("Nuevo email (deja vacío para no cambiar): ") or None
            nuevo_telefono = (
                input("Nuevo teléfono (deja vacío para no cambiar): ") or None
            )
            nueva_especialidad = (
                input("Nueva especialidad (deja vacío para no cambiar): ") or None
            )

            profesor_actualizado = actualizar_profesor(
                db,
                profesor_uuid,
                nuevo_nombre,
                nuevo_email,
                nuevo_telefono,
                nueva_especialidad,
            )

            if profesor_actualizado:
                print("Profesor actualizado correctamente.")
            else:
                print("No se encontró profesor con ese ID.")

        elif opcion == "4":
            profesores = listar_profesores(db)
            if not profesores:
                print("No hay profesores registrados.")
                continue

            profesor_id = input("ID del profesor a eliminar: ")
            try:
                profesor_uuid = uuid.UUID(profesor_id)
            except ValueError:
                print("ID inválido.")
                continue

            eliminado = eliminar_profesor(db, profesor_uuid)
            if eliminado:
                print("Profesor eliminado correctamente.")
            else:
                print("No se encontró profesor con ese ID.")

        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
    db.close()


def menu_materias(usuario, db):
    while True:
        print("\n=== MATERIAS ===")
        print("1. Listar materias")
        print("2. Crear materia")
        print("3. Actualizar materia")
        print("4. Eliminar materia")
        print("0. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            materias = listar_materias(db)
            if materias:
                print("\n--- Lista de Materias ---")
                for mat in materias:
                    print(
                        f"ID: {mat.id_materia} | Nombre: {mat.nombre} | Código: {mat.codigo} | Créditos: {mat.creditos} | Profesor: {mat.profesor.persona.nombre if mat.profesor else 'Sin asignar'}"
                    )
            else:
                print("No hay materias registradas.")

        elif opcion == "2":
            nombre = input("Nombre de la materia: ")
            codigo = input("Código: ")
            creditos = int(input("Créditos: "))
            profesores = listar_profesores(db)
            if not profesores:
                print("No hay profesores registrados.")
                continue
            profesor_id = input("ID del profesor (o Enter si no tiene): ") or None
            nueva_materia = create_materia(
                db, nombre, codigo, creditos, profesor_id, usuario.id_usuario
            )
            print(f" Materia creada: {nueva_materia.nombre}")

        elif opcion == "3":
            materias = listar_materias(db)
            if materias:
                print("\n--- Lista de Materias ---")
                for mat in materias:
                    print(
                        f"ID: {mat.id_materia} | Nombre: {mat.nombre} | Código: {mat.codigo} | Créditos: {mat.creditos} | Profesor: {mat.profesor.persona.nombre if mat.profesor else 'Sin asignar'}"
                    )
            else:
                print("No hay materias registradas.")
                continue  # Salir de la opción si no hay materias

            materia_id_input = input("ID de la materia a actualizar: ").strip()
            try:
                materia_id = uuid.UUID(materia_id_input)
            except ValueError:
                print("ID de materia no válido.")
                continue

            nombre = input("Nuevo nombre (Enter para omitir): ").strip() or None
            codigo = input("Nuevo código (Enter para omitir): ").strip() or None
            creditos_input = input("Nuevos créditos (Enter para omitir): ").strip()
            creditos = int(creditos_input) if creditos_input else None

            # Llamada correcta a actualizar_materia, sin tocar profesor_id
            materia_actualizada = actualizar_materia(
                db, materia_id, nombre, codigo, creditos
            )

            print("\n")
            print(
                "Materia actualizada correctamente."
                if materia_actualizada
                else "Materia no encontrada."
            )

        elif opcion == "4":
            materias = listar_materias(db)
            if materias:
                print("\n--- Lista de Materias ---")
                for mat in materias:
                    print(
                        f"ID: {mat.id_materia} | Nombre: {mat.nombre} | Código: {mat.codigo} | Créditos: {mat.creditos} | Profesor: {mat.profesor.persona.nombre if mat.profesor else 'Sin asignar'}"
                    )
            materia_id = input("ID de la materia a eliminar: ").strip()
            materia_eliminada = eliminar_materia(db, materia_id)
            if materia_eliminada:
                print(" Materia eliminada correctamente.")
            else:
                print(" Materia no encontrada.")

        elif opcion == "0":
            break
        else:
            print(" Opción no válida.")


def menu_notas(usuario, db):
    while True:
        print("\n===== MENÚ NOTAS =====")
        print("1. Listar notas")
        print("2. Agregar nota")
        print("3. Actualizar nota (solo valor)")
        print("0. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            notas = listar_notas(db)
            if notas:
                print("\n--- LISTADO DE NOTAS ---")
                for nota in notas:
                    print(
                        f"ID: {nota.id_nota}, Estudiante: {nota.estudiante.persona.nombre}, Materia: {nota.materia.nombre}, Valor: {nota.valor}"
                    )
            else:
                print("No hay notas registradas.")

        elif opcion == "2":
            estudiantes = listar_estudiantes(db)
            if not estudiantes:
                print("No hay estudiantes registrados.")
                continue
            print("\n--- LISTA DE ESTUDIANTES ---")
            for est in estudiantes:
                print(f"ID: {est.id_estudiante}, Nombre: {est.persona.nombre}")

            estudiante_id = input("ID del estudiante: ").strip()

            materias = listar_materias(db)
            if not materias:
                print("No hay materias registradas.")
                continue
            print("\n--- LISTA DE MATERIAS ---")
            for mat in materias:
                print(f"ID: {mat.id_materia}, Nombre: {mat.nombre}")

            materia_id = input("ID de la materia: ").strip()
            valor = float(input("Nota: "))

            nueva_nota = create_nota(db, estudiante_id, materia_id, valor)
            print(f"Nota agregada: {nueva_nota}")

        elif opcion == "3":
            notas = listar_notas(db)
            if not notas:
                print("No hay notas registradas.")
                continue
            print("\n--- LISTADO DE NOTAS ---")
            for nota in notas:
                print(
                    f"ID: {nota.id_nota}, Estudiante: {nota.estudiante.persona.nombre}, Materia: {nota.materia.nombre}, Valor: {nota.valor}"
                )

            id_nota = input("ID de la nota a actualizar: ").strip()
            nuevo_valor = float(input("Nuevo valor de la nota: "))
            nota_actualizada = actualizar_nota(db, id_nota, valor=nuevo_valor)
            if nota_actualizada:
                print(f"Nota actualizada: {nota_actualizada}")
            else:
                print("No se encontró la nota.")

        elif opcion == "0":
            break

        else:
            print("Opción inválida, intente nuevamente.")


def menu_auditoria():
    db = SessionLocal()
    print("\n=== AUDITORÍA ===")
    ver_auditoria(db)
    db.close()


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
            print(" Saliendo...")
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
