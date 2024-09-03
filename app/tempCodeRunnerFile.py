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
    