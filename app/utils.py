# lo llamamos utils porque tiene utilidades
# los archivos de utilidades normalmente solo tienen nombres

def get_population():
    keys = ['col', 'bol', 'per', 'mex']
    values = [300, 400, 500, 1000]
    return keys, values

# ya puede comportarse como modulos.
# A = 'hola'

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result

# asi vendra la informacion
[
    {
        'Country': 'col',
        'Population': 300
    },
    {
        'Country': 'bol',
        'Population': 300
    }
]

#### Graficar la poblacion historia de un pais dado

def get_population(country_dict):
    population_dict = {
        '2022': int(country_dict['2022 Population']), 
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population']),
    }
    
    keys = population_dict.keys()
    values = population_dict.values()
    return keys, values