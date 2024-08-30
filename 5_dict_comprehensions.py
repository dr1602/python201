# los comprehensions tambien pueden ser utilizados para crear diccionarios.

'''
Ejemplo

{key: value for var in iterable}
Elemento llave - valor
Ciclo donde se extraen elementos de cualquier iterables

el par clave valor lo obtendremos de un iterable

'''

# Sintaxis anterior

dict = {}

for i in range(1, 6):
    dict[i] = i * 2
# la llave es la i
# el valor es dado por i * 2

print(dict)
    
# ahora con sintaxis mas corta, con COMPRENHENSIONS

dict_v2 = { i: i * 2 for i in range(1, 6) }

print(dict_v2)

# partiremos la iteracion a a partir de una lista de paises

import random

countries = ['col', 'mex', 'bol', 'per']
population = {}

for country in countries:
    population[country] = random.randint(1, 100)
    
print(population)

# diccionario hecho con comprenhensions :)

population_v2 = { country: random.randint(1, 100) for country in countries }
print(population_v2)
    
    
# iteraremos con 2 listas y estas 2 listas haran diccionarios

names = ['Maria', 'Chichen', 'Kukulkan', 'Erendira']
ages = [6, 12, 24, 48]

'''
{
    'Maria': 6,
    'Chichen': 12,
    'Kukulkan': 24,
    'Erendira': 48,
}
'''

# Lo uniremos en un diccionario con DICTIONARY COMPREHENSION, veremos algo interesante de las lstas
# usaremos la funcion zip

print(zip(names, ages))
# <zip object at 0x7f9a2240a380>

print(list(zip(names, ages)))
# [('Maria', 6), ('Chichen', 12), ('Kukulkan', 24), ('Erendira', 48)]
# se creo una lista con tuplas, con primer el nombre y luego la edad

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)

nombres = ['Maria', 'Chichen', 'Kukulkan', 'Erendira']
edades = [6, 12, 24, 48]

new_dict_v2 = { nombres[i]:edades[i] for i in range(len(nombres))}
print(new_dict_v2)

new_dict_v3 = dict(zip(nombres,edades))
print(new_dict_v3)

new_dict_v5 = { nombres: edades for (nombres, edades) in zip(nombres, edades)}
print(new_dict_v5)

'''
Los tres métodos (new_dict_v2, new_dict_v3, new_dict_v5) tienen la misma complejidad en tiempo y espacio:

Complejidad de Tiempo: O(n)
Complejidad de Espacio: O(n)
Esto se debe a que cada método implica iterar sobre las listas una vez y construir un diccionario de tamaño n.
'''