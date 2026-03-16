import re

# 1. Validar cédula
def validar_cedula(cedula):
    if cedula.isdigit() and 8 <= len(cedula) <= 10:
        return True
    return False


# 2. Validar email
def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(patron, email):
        return True
    return False


# 3. Validar calificaciones
def validar_calificaciones(calificaciones):
    for nota in calificaciones:
        if nota < 0 or nota > 5:
            return False
    return True


# 5. Calcular promedio
def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    return round(promedio, 2)


# 6. Clasificar desempeño
def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Satisfactorio"
    else:
        return "Necesita mejorar"


# 4. Crear estudiante
def crear_estudiante(cedula, nombre, email, calificaciones):

    if not validar_cedula(cedula):
        return None

    if not validar_email(email):
        return None

    if not validar_calificaciones(calificaciones):
        return None

    promedio = calcular_promedio(calificaciones)

    estudiante = {
        "cedula": cedula,
        "nombre": nombre,
        "email": email,
        "promedio": promedio
    }

    return estudiante


# 7. Listar estudiantes
def listar_estudiantes(lista_estudiantes):

    if len(lista_estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    print("Cédula | Nombre | Promedio | Desempeño")

    for est in lista_estudiantes:
        desempeño = clasificar_desempeño(est["promedio"])
        print(f'{est["cedula"]} | {est["nombre"]} | {est["promedio"]} | {desempeño}')


# Buscar estudiante
def buscar_estudiante(lista_estudiantes, cedula):

    for est in lista_estudiantes:
        if est["cedula"] == cedula:
            desempeño = clasificar_desempeño(est["promedio"])
            print(f'{est["nombre"]} | Promedio: {est["promedio"]} | Desempeño: {desempeño}')
            return

    print("Estudiante no encontrado.")


# 8. Main
def main():

    estudiantes = []

    while True:

        print("\n--- SISTEMA DE GESTIÓN DE ESTUDIANTES ---")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Buscar estudiante por cédula")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            email = input("Email: ")
            notas_input = input("Calificaciones (separadas por coma): ")

            try:
                calificaciones = [float(n) for n in notas_input.split(",")]
            except:
                print("Error: formato de calificaciones inválido.")
                continue

            estudiante = crear_estudiante(cedula, nombre, email, calificaciones)

            if estudiante is None:
                print("Error: datos inválidos.")
            else:
                estudiantes.append(estudiante)
                desempeño = clasificar_desempeño(estudiante["promedio"])
                print(f'Estudiante agregado exitosamente. Promedio: {estudiante["promedio"]} | Desempeño: {desempeño}')

        elif opcion == "2":
            listar_estudiantes(estudiantes)

        elif opcion == "3":
            cedula_buscar = input("Cédula a buscar: ")
            buscar_estudiante(estudiantes, cedula_buscar)

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


# Ejecutar programa
if __name__ == "__main__":
    main()