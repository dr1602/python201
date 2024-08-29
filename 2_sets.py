# conjuntos que tienen elementos en comun como nombres de paises
# propieades de los conjuntos:
# se pueden modificar, no tienen un orden, no permite duplicados.

set_countries = {'México', 'Colombia', 'Bolivia', 'El Salvador', 'Guatemala', 'México', 'México' }

# no es un diccionario porque no tiene los pares clave - valor

print(set_countries)
print(type(set_countries))

# los valores repetidos los elimina, aun cuando fueron creados en la declaracion.

set_numbers = { 2, 4, 8, 16, 32, 64 , 128, 128}
print(set_numbers)
# e incluso los imprime de forma aleatoria

set_types = {1, 'hola', False, True, 12.12}
print(set_types)

# vamos a crearlo a partir de otro elemento
set_from_str = set('hooooola')
print(set_from_str)
# {'h', 'l', 'a', 'o'}

print(set_from_str)
# {'a', 'l', 'o', 'h'}

# podemos tener sets a partir de tuplas
set_from_tupla = set(('abc', 'efg', False, 12, 1, 0, 0, False))
print(set_from_tupla)
# {False, 1, 'efg', 'abc', 12}

print(set_from_tupla)
# {False, 1, 'efg', 'abc', 12}
# dentro de la misma ejecucion el set tiene el mismo orden

# a partir de una lista
numbers = [0, 2, 4, 4, 8, 8, 16, 16, 32, 64, 128, 256]
set_numbers1 = set(numbers)
set_numbers2 = set(numbers)

print(set_numbers1)
# {0, 32, 2, 64, 4, 128, 256, 8, 16}

unique_numbers1 = sorted(list(set_numbers1))

unique_numbers2 = list(set_numbers2)
unique_numbers2.sort()
# el método .sort() en Python ordena la lista en su lugar (modifica la lista original) y no devuelve una nueva lista ordenada
# si tratas de guardar este valor, ejecutandolo en una variable, te regresara "NONE"

print(unique_numbers1)
# [0, 2, 4, 8, 16, 32, 64, 128, 256]

print(unique_numbers2)

# en python para obtener valores unicos, la forma mas sencilla es transformando la lista con set,
# sin algoritmos especiales