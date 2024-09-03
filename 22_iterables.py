# hay iterables que se pueden controla manualmente desde el codigo, y no siendo necesariamente un ciclo

# iteracion sencilla
for i in range(1, 10):
    print(i)

# que es un range?

my_iter = range(1, 11)
print(my_iter)
# la impresion aqui es range, no se puede iterar, es el for lo que lo hace iterable

# para poderlo manejar manualmente y no por defecto como el for, usariamos la siguiente sintaxis
my_iter = iter(range(1, 5))
print(my_iter)
'''
nos da de vuelta un iterador
<range_iterator object at 0x7f0bafb42d00>

que es raro, tiene un nombre raro, pero es un iterador
'''

# cuando lo tenemos en ese formato podemos controlar la forma en que se jecuta, de forma manual
# se pueden generar iteraciones de forma manual

print(next(my_iter))
'''

<range_iterator object at 0x7f8095e9ed00>
1 <- se itera de forma manual, con una especie de for interno, con un next hasta que no tiene valores por iterar

'''

print(next(my_iter))
# 2
print(next(my_iter))
# 3
print(next(my_iter))
# 4

# esto en rendimiento no genera un rango de forma directa, no se tienen valores con un arary de mil valores
# los genera de forma progresiva, hace que el recurso en memoria no sea tan algto
# no hace un vector, lo hace a medida que genera el iterador
# es eficiente en memoria

'''
es importante entenderlo porque en las siguientes clases veremos archivos y estos s epueden leer
de esta manera, linea por linea, y se puede neceistar tener el iterador de forma manual, como la uno
y luego las demas.

cuando haces la iteracion manual, en algun momento hay un limite de iteracion y eso generara
una excepcion
'''

# excepecion

print(next(my_iter))
print(next(my_iter))

'''
Traceback (most recent call last):
  File "/root/Python201/tempCodeRunnerFile.py", line 44, in <module>
    print(next(my_iter))
StopIteration

hay que tomar en cuenta hasta cuando iterar sino se lanzara esa excepcion
'''