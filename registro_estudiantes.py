# Registro simple de estudiantes usando solo conceptos de la semana 5:
# variables, condicionales, input y ciclos

# guardaremos la información en listas paralelas
nombres = []
edades = []
calificaciones = []

# Pedir datos de 5 estudiantes
for i in range(5):
    print(f"\nEstudiante {i+1}")
    nombre = input("Nombre: ")

    # validar edad
    edad = int(input("Edad (5-100): "))
    while edad < 5 or edad > 100:
        print("Edad inválida, debe ser entre 5 y 100.")
        edad = int(input("Edad (5-100): "))

    # validar calificación
    calif = float(input("Calificación (0-5): "))
    while calif < 0 or calif > 5:
        print("Calificación inválida, debe ser entre 0 y 5.")
        calif = float(input("Calificación (0-5): "))

    nombres.append(nombre)
    edades.append(edad)
    calificaciones.append(calif)

# Buscar mejor y peor
indice_mejor = 0
indice_peor = 0
suma = 0.0
for j in range(5):
    suma += calificaciones[j]
    if calificaciones[j] > calificaciones[indice_mejor]:
        indice_mejor = j
    if calificaciones[j] < calificaciones[indice_peor]:
        indice_peor = j

promedio = suma / 5

print("\n--- Resultados ---")
print("Mejor calificación:", calificaciones[indice_mejor], "-", nombres[indice_mejor])
print("Peor calificación:", calificaciones[indice_peor], "-", nombres[indice_peor])
print("Promedio:", promedio)
