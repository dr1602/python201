# nos permiten empezar a modulizar la aplciacion y encerrar la logica en varios arhcivos
# un modiulo puede ser un archivo, python como tal vien con varios modulso com
import functools
import random

# para preguntar sobre el sistema operativa como donde esta trabajando este archivo
import sys
# imprime donde se esta ejecutado.
print(sys.path)

'''
['/root/Python201', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']
'''

# tiene que ver con expreisones regulares que son muy poderosas
import re
text = 'Mi numero de telefono es 311 123 456, el codigo del pais es 57, mi numero de la suerte es 1530125'
# obtendremos solo con los strings que coinciden con losnumeros de este texto
result = re.findall('[0-9]+', text)
# las expresiones regulares son transversales, se escriben igual en lenguajes como C
print(result)

'''
['311', '123', '456', '57', '1530125']
'''

# para manejo de horas y fechas
import time
# se encuentra en formato unix
timestamp = time.time()
print(timestamp)
'''
1725300506.3075504
pero se le puede dar un formato de lectura mas para los humanos
'''

# para pedir el tiempo local
local = time.localtime()
# para ajustar el formato
result = time.asctime()
print(result)

'''
Mon Sep  2 12:10:17 2024
es la hora que corre en servidor, no la hora en la que corre python, sobre todo para
ambientes virtuales
'''

# para manejar listas
import collections

numbers = [1, 2, 1, 2, 2, 1, 5, 7, 7, 8, 9, 5, 6, 13, 15, 21]
counter = collections.Counter(numbers)
print(counter)

'''
Counter({1: 3, 2: 3, 5: 2, 7: 2, 8: 1, 9: 1, 6: 1, 13: 1, 15: 1, 21: 1})
diccionario con la lista de resultados
'''
