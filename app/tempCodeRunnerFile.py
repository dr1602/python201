
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
    print(data[3])