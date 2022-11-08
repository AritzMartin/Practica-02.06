diccionario = {'euro':'€', 'dollar':'$', 'yen':'¥'}
divisa = input('Escriba el nombre de la divisa:\n')

if divisa.lower() in diccionario:
    print(diccionario[divisa])
else:
    print('No tengo esa divisa')