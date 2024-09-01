# se puede retornar mas de valor en una funcion y ver a profundidad sus argumentos
# podemos definir parametros con valores por defecto

def find_volume(length = 1, width=1, depth = 1):
    return length * width * depth

# como da return, puedo almacenar el resultado en una variable

result = find_volume()
print(result)

result_2 = find_volume(2, 3, 4)
print(result_2)

# podemos mandar solo un valor y dejar los demas por defecto

result_3 = find_volume(width=3)
print(result_3)

# podriamos retornar mas de una funcion, podemos decirle que individualmente devuelvaotras cosas

def find_volume2(length = 1, width=1, depth = 1):
    return length * width * depth, width, 'hola'

result = find_volume2(width=10)
# nos devuelve una tupla con los valores
'''
(10, 10, 'hola')
'''
print(result[0])

# tambien se puede asignar una respuesta con comas al guardar en variable

result_2, width, texto = find_volume2(width=10)
print(result_2)
print(width)
print(texto)
