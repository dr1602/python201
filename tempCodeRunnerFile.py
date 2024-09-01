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
