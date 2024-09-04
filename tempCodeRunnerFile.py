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