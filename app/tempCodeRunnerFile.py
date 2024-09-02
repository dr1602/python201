# como podemos empezar a llmar otros modulos en python usamos la palbra clave import
import utils
# al importarlo podemos empzar a ejecutarlo

keys, values = utils.get_population()

print(keys, values)
# ['col', 'bol', 'per', 'mex'] [300, 400, 500, 1000]

# print(utils.A)
# hola

# se actualizo automaticamente el nombre de los archivos

data = [
    {
        'Country': 'col',
        'Population': 300
    },
    {
        'Country': 'bol',
        'Population': 300
    },
    {
        'Country': 'arg',
        'Population': 400
    }
]

reusult = utils.population_by_country(data, 'col')
print(reusult)

# [{'Country': 'col', 'Population': 300}]

# ahora lo haremos de forma dinamica en lugar de solo poner colombia

country = input('Ingrese el nombre del pais del que quiere conocer su poblacion:')
result_v2 = utils.population_by_country(data, country)

print(result_v2)