def registro_estudiantes():
    """Programa para registrar cinco estudiantes con validación.

    - Pide nombre, edad y calificación de 5 estudiantes.
    - Edad debe estar entre 5 y 100 inclusive.
    - Calificación debe estar entre 0 y 5 inclusive.
    - Si se ingresan datos inválidos, se pide de nuevo.
    - Al final muestra:
        * Estudiante con la calificación más alta.
        * Estudiante con la calificación más baja.
        * Calificación promedio de todos.
    """
    estudiantes = []  # cada ítem será un diccionario con keys: nombre, edad, calif

    for i in range(1, 6):
        print(f"\nIngresando datos para el estudiante #{i}")
        nombre = input("Nombre: ").strip()

        # validar edad
        while True:
            try:
                edad = int(input("Edad (5-100): "))
            except ValueError:
                print("Debe ser un número entero.")
                continue
            if 5 <= edad <= 100:
                break
            print("Edad inválida, debe estar entre 5 y 100.")

        # validar calificación
        while True:
            try:
                calif = float(input("Calificación (0-5): "))
            except ValueError:
                print("Debe ser un número válido.")
                continue
            if 0 <= calif <= 5:
                break
            print("Calificación inválida, debe estar entre 0 y 5.")

        estudiantes.append({"nombre": nombre, "edad": edad, "calif": calif})

    # calcular estadísticas
    mejor = max(estudiantes, key=lambda e: e["calif"])
    peor = min(estudiantes, key=lambda e: e["calif"])
    promedio = sum(e["calif"] for e in estudiantes) / len(estudiantes)

    print("\n--- Resultados ---")
    print(f"Mejor calificación: {mejor['calif']}  Estudiante: {mejor['nombre']}")
    print(f"Peor calificación: {peor['calif']}  Estudiante: {peor['nombre']}")
    print(f"Calificación promedio: {promedio:.2f}")


if __name__ == "__main__":
    registro_estudiantes()
