# funcion para leer csv

import csv

path = './app/data.csv'

def read_csv(path):
    with open(path,'r') as csvfile:
        # delimiter es la forma e la que los datos estan seprados como , pero a veces puede ser con ;
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print('***' * 9)
            print(row)
            # ejeceutar archivo como script en terminal
            
# read_csv(path)
            
if __name__ == '__main__':
    read_csv(path)
    
# lee cada una de las columnas como un array
# tiene toda la informacion separada en un tipo de lista
# ahora la transformaremos en diccionario en lugar de un array de datos, para poder acceder con la clave de la columna

'''
tenemos que leerlo en una lista que tenga diccionarios para que sea de mas facil lectura
la llave del diccionario va a ser el nombre de laa columna

[
    {
        'Country': 'Colombia',
        'Capital': 'Bogota',
        '2022 Population': 3000,
        'World Population Percentage': 0.12
    },
        {
        'Country': 'Bolivia',
        'Capital': 'Sucre',
        '2022 Population': 500,
        'World Population Percentage': 0.01
    },
]
'''

import csv

path = './app/data.csv'

def read_csv(path):
    with open(path,'r') as csvfile:
        # reder es un iterable
        reader = csv.reader(csvfile, delimiter=',')
        #la primer fila es el nombre de las columnas
        header = next(reader)
        
        # para generar un nuevo diccionario que se guarde, seria con
        data = []
        for row in reader:
            # los unira en un array de tuplas
            iterable = zip(header, row)
            # print(list(iterable))
            # generaremos un diccionario a partir del iterable
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
            # print(country_dict)
            # print('***' * 9)
            # print(row)
        return data

if __name__ == '__main__':
    data = read_csv(path)
    print(data[0:3])