# vamos a importar el paquete
# import pkg

# podriamos empezar a importar de la siguiente manera las funciones y sus modulos

from package.mod_1 import func_1, func_2
import package.mod_1
from package.mod_2 import func_3, func_4

print(func_1())
print(func_2())

'''
Funciton 1
Funciton 2
'''

print(func_3())
print(func_4())

'''
Funciton 3
Funciton 4
'''

# asi se empaqueta una serie de logica.
# ahora es facil hacer esa importancia pero antes se tenia que definir y crear un archivo init .pay
# pero ahora no fue necesario porque estamos en una version superior de python 3.3
# en versiones anteriores hay que agregar ese archivo

# la variable de __init__ sin importar que archivo se llame de package, se va a inicilaizars
# no se inicializa dos veces, se inicializauna vez

import package
print(package.URL)
'''
la url hace parte del paquete

Se inicio paquete
platzi.com
'''

# tambien podemos usarlo para definir un name space, donde los espacios de nombres son itneresantes
# y de veriamos hacer mayor uso de ellos

print(package.mod_1.func_1())

# esto es debil y puede causar errores pero solo sirve porque antes ya importamos esos modulos

'''
Se inicio paquete
platzi.com
Traceback (most recent call last):
  File "/root/Python201/tempCodeRunnerFile.py", line 14, in <module>
    print(package.mod_1.func_1())
AttributeError: module 'package' has no attribute 'mod_1'

genera error porque no hay importacion explicita
'''

# como se puede automatizar para que no se genere error
# con la modifificaicon ya no genera error, se puede hacer la importacion con name space
# sirve para cuando hay funciones en distintos modulos con mismo nombre

'''
Se inicio paquete
platzi.com
Funciton 1
'''