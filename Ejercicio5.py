diccionario = {}

print('Introduzca la palabra y su traducción con el siguiente formato: '
      'palabracastellano:traduccióningles')
print('Para acabar con el proceso escriba: terminar')
while True:
    palabra = input('')
    if palabra == 'terminar':
        break
    traduccion = palabra.split(':')
    diccionario[traduccion[0]] = traduccion[1]

frase = input('Escriba una frase en castellano:\n')

for palabra in frase.split(' '):
    if palabra in diccionario.keys():
        print(diccionario[palabra], end=" ")
    else:
        print(palabra, end=" ")

