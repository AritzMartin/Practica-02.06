diccionario = {'pan':1.40, 'huevos':2.30, 'cebolla':0.85, 'aceite':4.35}
articulo = str.lower(input('Que artículo quiere?\n'))
cantidad = int(input('Qué cantidad quiere?\n'))

if articulo in diccionario:
    print(diccionario[articulo] * cantidad)
else:
    print("No tenemos ese producto")