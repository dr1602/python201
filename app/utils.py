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
