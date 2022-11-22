base_datos = []
clase = {}

print("********************************")
print("             MENÚ                 ")
print('  [1]. Añadir alumno/a          ')
print('  [2]. Eliminar alumno/a        ')
print('  [3]. Mostrar alumno/a         ')
print('  [4]. Listar todo el alumnado  ')
print('  [5]. Listar alumnado aprobado ')
print('  [6]. Terminar                 ')
print('********************************')

usr_option = int(input("Eliga una opcion :\n"))
while True:
    if usr_option == 1:
        clase['nif'] = input('Escribe el NIF del alunmo/a:\n')
        clase['nombre'] = input('Escribe el nombre del alunmo/a:\n')
        clase['apellidos'] = input('Escribe los apellidos del alunmo/a:\n')
        clase['telefono'] = input('Escribe el número de teléfono delalunmo/a:\n')
        clase['correo'] = input('Escribe el correo del alunmo/a:\n')
        clase['aprobado'] = input('El alunmo/a ha aprobado?\n')
    if usr_option == 2:
        nif = input('Escribe el NIF del alunmo/a:\n')
        clase.keys()
        if nif in clase.keys():
            del clase

    if usr_option == 6:
        break
    else:
        print('ERROR')

