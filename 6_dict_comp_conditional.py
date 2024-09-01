'''
Trabajaremos con dictionary comprehensions pero ahora con condicionales

con estructura
{key : value for var in iterable if condition}

'''

import random

# diccionario hecho con comprenhensions :)

countries = ['col', 'mex', 'bol', 'per']
population = {}

population_v2 = { country: random.randint(1, 100) for country in countries }
print(population_v2)

## generaremos otro diccionario pero con paises con poblacion mayor a 20

resultado = { country: population for (country, population) in population_v2.items() if population > 20 }

print(resultado)

text = 'Hola, soy David'
vocales = { c: c.upper() for c in text if c in 'aeiou' }
print(vocales)

# {'o': 'O', 'a': 'A', 'i': 'I'}
'''
este valor es asi porque es un diccionario y recuerda que en los diccionarios los numeros 
lo valores no se pueden repetir
'''

# reto, transformarlo en mayuscula sino tener el numero de frecuencia de la letra

text = 'Hola, soy David'
vocales = { c: text.count(c) for c in text if c in 'aeiou' }
print(vocales)