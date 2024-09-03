with open('./text.py', 'w+') as file:
    for line in file:
        print(line)
    # literalmente escribe al final del ultimo teto pero no crea una nueva linea
    # para generar nuevas lineas tenemos que hacer esto
    file.write("print('Hola Mundo')\n")