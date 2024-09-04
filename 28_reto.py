# generar columna para crear grafico de tortas

import inquirer
import csv
import matplotlib.pyplot as plt

path = './app/data.csv'

def menu_options():
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

def menu_regions():
    questions = [
    inquirer.List('column',
                    message="¿Qué columna deseas graficar?",
                    choices=[
                        'Asia',
                        'Europe',
                        'Africa',
                        'Oceania',
                        'North America',
                        'South America',
                    ],
                ),
    ]
    options = inquirer.prompt(questions)
    regions = options["column"]

    return(regions)

def country_historical_population(path):
    
    choice = menu_options()
    region = menu_regions()

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

        countries = []
        data = []
        
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            if country_dict['Continent'] == region:
                countries.append(country_dict['Country/Territory'])
                try:
                    if choice == 'Growth Rate' or 'World Population Percentage' or 'Density (per km²)':
                        data.append(float(country_dict[choice]))
                    else:
                        data.append(int(country_dict[choice]))
                except ValueError:
                    print(f"Error al convertir el valor: {country_dict[choice]} de la columna {choice}")
                    break
        
        try:
            if choice in ['Growth Rate', 'World Population Percentage', 'Density (per km²)']:
                final_data = { countries[i]:data[i] for i in range(len(data)) }
                sorted_data = dict(sorted(final_data.items(), key=lambda item: item[1], reverse=True))
                
                fig, ax = plt.subplots()
                # Cambiamos a un gráfico de tortas
                ax.pie(sorted_data.values(), labels=sorted_data.keys(), autopct='%1.1f%%', startangle=90)
                ax.axis('equal')  # Para que el gráfico de pie sea un círculo perfecto
                
                plt.show()
            else:
                final_data = { countries[i]:data[i] for i in range(len(data)) }
                sorted_data = dict(sorted(final_data.items(), key=lambda item: item[1], reverse=True))
                
                fig, ax = plt.subplots()
                ax.bar(sorted_data.keys(), sorted_data.values())
                
                plt.show()
        except:
            print('error')
        
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


###

import csv

def country_historical_population():
    
    choice = 'Continent'

    with open('./app/data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

        countries = []
        data = []
        
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            countries.append(country_dict['Country/Territory'])
            try:
                if choice == 'Continent':
                    data.append(country_dict[choice])
            except ValueError:
                print(f"Error al convertir el valor: {country_dict[choice]} de la columna {choice}")
                break
        
        output = []
        for x in data:
            if x not in output:
                output.append(x)
                
        print(output)


country_historical_population()


###

import inquirer
import csv
import matplotlib.pyplot as plt

path = './app/data.csv'

def menu_options():
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

def menu_regions():
    questions = [
        inquirer.List('column',
                      message="¿Qué región deseas graficar?",
                      choices=[
                          'Asia',
                          'Europe',
                          'Africa',
                          'Oceania',
                          'North America',
                          'South America',
                      ],
                      ),
    ]
    options = inquirer.prompt(questions)
    regions = options["column"]

    return regions

def country_historical_population(path):
    choice = menu_options()
    region = menu_regions()

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

        countries = []
        data = []

        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            if country_dict['Continent'] == region:
                countries.append(country_dict['Country/Territory'])
                try:
                    if choice in ['Growth Rate', 'World Population Percentage', 'Density (per km²)']:
                        data.append(float(country_dict[choice]))
                    else:
                        data.append(int(country_dict[choice]))
                except ValueError:
                    print(f"Error al convertir el valor: {country_dict[choice]} de la columna {choice}")
                    break

        try:
            final_data = {countries[i]: data[i] for i in range(len(data))}
            sorted_data = dict(sorted(final_data.items(), key=lambda item: item[1], reverse=True))

            fig, ax = plt.subplots()

            # Crear gráfico de tortas en lugar de barras
            ax.pie(sorted_data.values(), labels=sorted_data.keys(), autopct='%1.1f%%', startangle=140)

            plt.title(f"Gráfico de tortas para {choice} en {region}")
            plt.axis('equal')  # Para que el gráfico sea un círculo
            plt.show()

        except Exception as e:
            print(f'Error: {e}')

        return sorted_data

country_historical_population(path)
