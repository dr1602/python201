# veamos los tipos de errores y como podemos levantar nuestros propios tipos de errores
# estos errores ya los hemos visto en el pasado como dividir entre cero

# error de sintaxis
# print(0 / 0))

'''
  File "/root/Python201/tempCodeRunnerFile.py", line 3
    print(0 / 0))
                ^
SyntaxError: unmatched ')'

'''

# error de division con cero

# print(0 / 0)

'''
se presenta explicita e implicitamente cuando hacemos esas divisiones en cero

Traceback (most recent call last):
  File "/root/Python201/tempCodeRunnerFile.py", line 1, in <module>
    print(0 / 0)
ZeroDivisionError: division by zero
'''

# Name error
# referencia a una variable que no existe

# print(result)

'''
Traceback (most recent call last):
  File "/root/Python201/tempCodeRunnerFile.py", line 2, in <module>
    print(result)
NameError: name 'result' is not defined

cuando hay un error un programa se termina, python no lo ejecuta cuando ve un error
'''

# print(result)
# print('hola')

# se termina antes de imprimir hola

# otro tipo de error es el assert

suma = lambda x,y: x + y
# assert es para veriticar
assert suma(2,2) == 4
print('hola')

# no sale ningun error y deja imrpimir mas lineas, no manda error
# hola

## todo paso de la forma correcta

suma = lambda x,y: x + (y * 2)
assert suma(2,2) == 4
print('hola')

'''
aqui te da assertion errors, que la funcion no esta funcionando como deberia

se puede emepzar a tener una disciplina conocida como pruebas unitarias para saber que
los metodos estan sirviendo de la forma en la que deberian

podrian ser herramientas, pero ahora se puede usar esa palabra clave
'''

suma = lambda x,y: x + (y * 1)
assert suma(2,2) == 4
print('hola')

# tambien podemos lanzar nuestras propias excepciones

age = 10

if age < 18:
    # vamos a lanzar una excepcion, un error como el de python pero que hacemos y que cumple con las reglas de negocio como no tener menores de edad.
    # para avantar error usamos la palabra reservada raise y excepcion
    raise Exception('No se permiten menores de edad')

'''
Traceback (most recent call last):
  File "/root/Python201/tempCodeRunnerFile.py", line 7, in <module>
    raise Exception('No se permiten menores de edad')
Exception: No se permiten menores de edad

es diferente a las que lanza naturalmente python
'''

'''
imagina que tienes el serivicio de una gran compania, y esta escrita con logica en python
con algun error seria valido que toda la app caiga?

eso no deberia pasar, que deniegue todo con error, hat saber manejar esas excepciones.
'''
