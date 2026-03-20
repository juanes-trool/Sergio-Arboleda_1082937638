estudiantes=['Juan','Maria','Pedro','Ana','Luis','Sofia']

# Agregar un nuevo estudiante al final 
estudiantes.append('Carlos')
print(estudiantes)
estudiantes.append('Lucia')
print(estudiantes)
estudiantes.append('Diego')
print(estudiantes)
estudiantes.append('Valentina')
print(estudiantes)

print(len(estudiantes)) # Imprime la cantidad de estudiantes 

if 'Maria' in estudiantes:
    print('Maria está en la lista de estudiantes.')

estudiantes.remove('Pedro') # Elimina la prmera ocurrencia de 'Pedro'
print(estudiantes)