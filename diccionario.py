persona = {"nombre": "Juan", "edad": 30, "ciudad": "Santa Marta"}

# iterar sobre las claves 
for clave in persona:
    print(clave)

# iterar sobre pares clave-valor
for clave, valor in persona.items():
    print(clave + ": " + str(valor))