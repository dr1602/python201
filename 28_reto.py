# generar columna para crear grafico de tortas

import inquirer
import csv
import matplotlib.pyplot as plt

path = './app/data.csv'

def menu():
    questions = [
    inquirer.List('column',
                    message="¿Qué columna deseas graficar?",
                    choices=[
                        '2022 Population',
                        '2020 Population',
                        '2015 Population',
                        '2010 Population',
                        '2000 Population',
                        '1990 Population',
                        '1980 Population',
                        '1970 Population',
                        'Area (km²)',
                        'Density (per km²)',
                        'Growth Rate',
                        'World Population Percentage',
                    ],
                ),
    ]
    options = inquirer.prompt(questions)
    choice = options["column"]

    return(choice)

def country_historical_population(path):
    
    choice = menu()

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

        countries = []
        data = []
        
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            countries.append(country_dict['Country/Territory'])
            try:
                if choice == 'Growth Rate' or 'World Population Percentage' or 'Density (per km²)':
                    data.append(float(country_dict[choice]))
                else:
                    data.append(int(country_dict[choice]))
            except ValueError:
                print(f"Error al convertir el valor: {country_dict[choice]} de la columna {choice}")
                break
        
        final_data = { countries[i]:data[i] for i in range(len(data)) }
        sorted_data = dict(sorted(final_data.items(), key=lambda item: item[1], reverse=True))
        
        fig, ax = plt.subplots()
        ax.bar(sorted_data.keys(), sorted_data.values())
        
        plt.show()
        
        return sorted_data

country_historical_population(path)

######

import inquirer
import csv
import matplotlib.pyplot as plt

path = './app/data.csv'

def menu():
    questions = [
        inquirer.List('column',
                      message="¿Qué columna deseas graficar?",
                      choices=[
                          '2022 Population',
                          '2020 Population',
                          '2015 Population',
                          '2010 Population',
                          '2000 Population',
                          '1990 Population',
                          '1980 Population',
                          '1970 Population',
                          'Area (km²)',
                          'Density (per km²)',
                          'Growth Rate',
                          'World Population Percentage',
                      ],
        ),
    ]
    options = inquirer.prompt(questions)
    choice = options["column"]

    return choice

def country_historical_population(path):
    
    choice = menu()

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        
        countries = []
        data = []
        
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            countries.append(country_dict['Country/Territory'])
            
            # Condicional para elegir el tipo de conversión
            try:
                if choice in ['Growth Rate', 'World Population Percentage', 'Density (per km²)']:
                    data.append(float(country_dict[choice]))  # Usa float() para columnas con decimales
                else:
                    data.append(int(country_dict[choice]))  # Usa int() para columnas con enteros
            except ValueError:
                print(f"Error al convertir el valor: {country_dict[choice]} de la columna {choice}")
                continue
        
        # Crear el diccionario final de datos
        final_data = {countries[i]: data[i] for i in range(len(data))}
        
        # Ordenar los datos por valores
        sorted_data = dict(sorted(final_data.items(), key=lambda item: item[1], reverse=True))

        # Graficar los datos
        fig, ax = plt.subplots()
        ax.bar(sorted_data.keys(), sorted_data.values())
        
        plt.xticks(rotation=90)
        plt.show()
        
        return sorted_data

country_historical_population(path)
