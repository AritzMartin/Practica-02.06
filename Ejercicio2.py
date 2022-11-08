nombre = input('Cual es su nombre?\n')
edad = input('Cual es su edad?\n')
direccion = input('Cual es su dirección?\n')
telefono = input('Cual es su número de teléfono?\n')

diccionario = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}

print(diccionario['nombre'], 'tiene', diccionario['edad'], 'vive en', diccionario['direccion']
      , 'y su número de telefono es', diccionario['telefono'])
