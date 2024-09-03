# como escribir dentro de un archivo, para trabajar la parte de writing
# recuerda revisar siempre el archivo fuente para ver si coincide con el texto que importas

with open('./text.txt') as file:
    for line in file:
        print(line)
        
    # $ para escribir ahi tenenmos file.write
    
    file.write('Nuevo texto en el archivo')
    # aqui nos dice que no tenemos permisos de escritura
    
'''
Traceback (most recent call last):
  File "/root/Python201/tempCodeRunnerFile.py", line 10, in <module>
    file.write('Nuevo texto en el archivo')
io.UnsupportedOperation: not writable

porque cuando hacemos open solo viene con permisso de lectura
'''

# otra forma para solo tener permiso de lectura

with open('./text.txt', 'r') as file:
    for line in file:
        print(line)
    file.write('Nuevo texto en el archivo')
    
    # es leible no escribible
    
# para tener permisos de escritura se requiere:
with open('./text.txt', 'w') as file:
    for line in file:
        print(line)
        
    # ahora es escribible pero no leible y borra el contenido  
    #BORRA EL CONTENIDO
    
    file.write('Nuevo texto en el archivo')
    
with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
        
    # ahora es escribible pero no leible y borra el contenido
    
    file.write('Nuevo texto en el archivo')

    # literalmente escribe al final del ultimo teto pero no crea una nueva linea
    # para generar nuevas lineas tenemos que hacer esto
    
    file.write('Nuevo texto en el archivo en nueva linea\n')
    file.write('Nueva linea\n')
    file.write('Y otra nueva linea\n')
    
    # por cierto, estos comandos luego de escribir no imrpimen el archivo, por eso no seve
    # el permiso de r+ nos permite leer y escribir, y esciribr es agregar lineas repsetanod el formato el archivo
    
    # con w+ se sobre escribira todo el archivo pero tendremos todos los permisos
    
with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
    # literalmente escribe al final del ultimo teto pero no crea una nueva linea
    # para generar nuevas lineas tenemos que hacer esto
    
    file.write('Una vez comenzada la batalla, aunque estés ganando, de continuar por mucho tiempo,\n')
    file.write('desanimará a tus tropas y embotará tu espada. Si estás sitiando una ciudad, agotarás\n')
    file.write('tus fuerzas. Si mantienes a tu ejército durante mucho tiempo en campaña, tus\n')
    file.write('suministros se agotarán.\n')
    
with open('./text.py', 'w+') as file:
    for line in file:
        print(line)
    # literalmente escribe al final del ultimo teto pero no crea una nueva linea
    # para generar nuevas lineas tenemos que hacer esto
    file.write("print('Hola Mundo')\n")