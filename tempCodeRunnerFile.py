import csv

def read_csv(path):
    # Tu código aquí 👇
    total = 0
    
    with open(path, 'r') as csvfile:
       lines = csv.reader(csvfile, delimiter=',')
       for row in lines:
           total += int(row[1])     
    
    return total

response = read_csv('./data.csv')
print(response)