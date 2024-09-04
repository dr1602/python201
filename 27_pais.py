# tenemos que seleccionar solo un pais del csv y tomar su crecimiento poblacion de los anios para poderlo
# graficar en el bar char
# para solucionarlo hay que entender que ya tenemos toda esa inforamcion en formato diccionario donde tenemos como clave 
# tenemos como clave el nombre d el columa y su valor para lograr el reto donde queremos hacer una grafica del crecimiento poblacional
# tenemos que transformarlo en algo donde solo tengamos los valores anio valor

###################################
# Propuesta de solucion 1

import csv
import matplotlib.pyplot as plt

path = './app/data.csv'

def country_historical_population(path, country):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        
        years = ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']
        data = []
        
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            if country_dict['Country/Territory'] == country:
                data.append(int(country_dict['2022 Population']))
                data.append(int(country_dict['2020 Population']))
                data.append(int(country_dict['2015 Population']))
                data.append(int(country_dict['2010 Population']))
                data.append(int(country_dict['2000 Population']))
                data.append(int(country_dict['1990 Population']))
                data.append(int(country_dict['1980 Population']))
                data.append(int(country_dict['1970 Population']))
        
        fig, ax = plt.subplots()
        ax.bar(years, data)
        
        final_data = { years[i]:data[i] for i in range(len(data)) }
        
        plt.show()
        
        return final_data

data = country_historical_population(path, 'Colombia')
print(data)

######################################
# Propuesta de solucion 2

import csv
import matplotlib.pyplot as plt

def country_historical_population(path, country):
    # Define los años y los índices correspondientes en las filas del CSV
    years_indices = {
        '2022': 5,  # Índice basado en tu CSV, ajusta si cambian las columnas
        '2020': 6,
        '2015': 7,
        '2010': 8,
        '2000': 9,
        '1990': 10,
        '1980': 11,
        '1970': 12
    }

    # Diccionario final de población
    final_data = {}

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Salta el encabezado

        for row in reader:
            # Verifica si el país coincide
            if row[2] == country:
                # Extrae las poblaciones según los años requeridos
                final_data = {year: int(row[index]) for year, index in years_indices.items()}
                break  # Detiene la iteración una vez encontrado el país
            
        fig, ax = plt.subplots()
        ax.bar(final_data.keys(), final_data.values())
        
        plt.show()

    return final_data

# Ejecuta la función
data = country_historical_population('./app/data.csv', 'Colombia')
print(data)
