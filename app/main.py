# como podemos empezar a llmar otros modulos en python usamos la palbra clave import
import utils
# al importarlo podemos empzar a ejecutarlo

# una forma de modulariza, y que solo se ejecute de forma explicita es metiendo todo en una funcion

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

def run():
    keys, values = utils.get_population()

    print(keys, values)
    # ['col', 'bol', 'per', 'mex'] [300, 400, 500, 1000]

    # print(utils.A)
    # hola

    # se actualizo automaticamente el nombre de los archivos

    reusult = utils.population_by_country(data, 'col')
    print(reusult)

    # [{'Country': 'col', 'Population': 300}]

    # ahora lo haremos de forma dinamica en lugar de solo poner colombia

    country = input('Ingrese el nombre del pais del que quiere conocer su poblacion:')
    result_v2 = utils.population_by_country(data, country)

    print(result_v2)
    # [{'Country': 'arg', 'Population': 400}]
    
    '''
    para que main se ejecute como script, que se ejecute de forma directa
    se ejecute pero ya no pasa nada ya que no existe nada que controle la ejecucion del archivo
    
    python3 app/main.py
    
    no te devuleve nada
    
    lo que queremos los siguiente que si se ejecuta desde example, que example controle la ejecucion de main
    
python3 app/example.py
[{'Country': 'col', 'Population': 300}, {'Country': 'bol', 'Population': 300}, {'Country': 'arg', 'Population': 400}]
[{'Country': 'col', 'Population': 300}, {'Country': 'bol', 'Population': 300}, {'Country': 'arg', 'Population': 400}]
['col', 'bol', 'per', 'mex'] [300, 400, 500, 1000]
[{'Country': 'col', 'Population': 300}]


para tener la dualidad, que example, que usa main se peude ejecutar y controlar la ejeuccion de main, pero 
que main tambien se pueda ejecutar

para ejecutarlo sera con un if de varios metodos de python

    '''
    
def runV2():
    keys, values = utils.get_population()
    print(keys, values)

    reusult = utils.population_by_country(data, 'col')
    print(reusult)

    country = input('Ingrese el nombre del pais del que quiere conocer su poblacion:')
    result_v2 = utils.population_by_country(data, country)

    print(result_v2)

if __name__ == '__main__':
    # donde ponemos y ejecutamos run, y dice al main que s es ejecutado desde la terminal que ejecute run, sino, no
    runV2()
    
'''
app/main.py
['col', 'bol', 'per', 'mex'] [300, 400, 500, 1000]
[{'Country': 'col', 'Population': 300}]
Ingrese el nombre del pais del que quiere conocer su poblacion:

sin el if no se podria ejecutar como script
'''

import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('./app/data.csv')
    country = input('Type Country => ')
    
    result = utils.population_by_country(data, country)
    
    if len(result) > 0:  
        country = result[0]
        keys, values = utils.get_population(country)
        charts.generate_bar_char(keys, values)
        
if __name__ == '__main__':
    run()
    