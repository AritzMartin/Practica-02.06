base_datos = []

print('********************************')
print('          MENÚ                  ')
print('  [1]. Añadir alumno/a          ')
print('  [2]. Eliminar alumno/a        ')
print('  [3]. Mostrar alumno/a         ')
print('  [4]. Listar todo el alumnado  ')
print('  [5]. Listar alumnado aprobado ')
print('  [6]. Terminar                 ')
print('********************************')

if input() == 1:
    nif = input('Escribe el NIF del alunmo/a:\n')
    nombre = input('Escribe el nombre del alunmo/a:\n')
    apellidos = input('Escribe los apellidos del alunmo/a:\n')
    telefono = input('Escribe el número de teléfono del alunmo/a:\n')
    correo = input('Escribe el correo del alunmo/a:\n')
    aprobado = input('El alunmo/a ha aprobado?\n')
else:
    print('ERROR')

