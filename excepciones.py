# manejo y control de errores con python
# vamos a controlar y manejar los errores y evitar que se detenga el programa

print(0/0)

print('hola')

'''
Traceback (most recent call last):
  File "/root/Python201/tempCodeRunnerFile.py", line 2, in <module>
    print(0/0)
ZeroDivisionError: division by zero
'''

# podemos manejar y controlar el error:

try:
    print(0/0)
except ZeroDivisionError as error:
    # aqui decimos que queremos hacer con el errror
    # una buena practica para el manejo de errores es hacer tracking o registrar errores en sistema aparte y tener un report e de error , sin tirar el servicio
    print(error)
    # aqui puedes gestionar el error de la forma que quieras
    
# si se ejecuto esta linea, aun con el error, por el manejor de error
print('hola')

'''
division by zero
hola
'''

assert 1 != 1, 'Uno es igual que uno'

# no se imprime esta lina de codigo porque no hay manjeo de excepcion pero si busca el error
print('hola')

try:
    assert 1 != 1, 'Uno es igual que uno'
except AssertionError as error:
    print(error)
    
print('hola nuevamente')

'''
hola
Uno es igual que uno
hola nuevamente

no detuvo la secuencia del programa y asi podemos capturar otros errores

por ejemplo, como capturariamos el propio
'''

try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except Exception as error:
    print(error)
    
# La ejecucion llega hasta el final

'''
pero puede ser cansado poner una linea por tipo de error,para eso podemos poner toda nuestra logica
y poner diferentes tipos de errores
'''


try:
    print(0/0)
    assert 1 != 1, 'Uno es igual que uno'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print('hola nuevamente')


'''
hola nuevamente
division by zero

como encuentra un error, no procede con las lineas internas del try pero si continua con las que estan
afuera del bloque sin ningun problema
'''

try:
    print(0/0)
    assert 1 != 1, 'Uno es igual que uno'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except ZeroDivisionError or AssertionError or Exception as error:
    print(error)

print('hola nuevamente')

'''
division by zero
hola nuevamente
'''
