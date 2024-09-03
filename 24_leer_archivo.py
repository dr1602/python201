# leeremos un archivo del tipo txt
# necesitaremos un archivo para leer, como archivo hermano

# para leer el archivo
file = open('./text.txt')
print(file.read())
file.close()

# tambien se puede leer linea por linea de forma manual como el iterador next, que vimos

file = open('./text.txt')
print(file.readline())
print(file.readline())
print(file.readline())

# es importante saber cuando cerrar el crchivo, cuando dejaremos de leerlo

file.close()
# no se ve la diferencia pero cerrara el archivo y dejara libre el espacio en memoria

'''
leer todo el archivo con todas las lineas, con el primer metodo puede ser muy pesado pero el read line
puede ir linea por linea y requiere menos espacio en memoria

tambien podemos usar un for
'''

file = open('./text.txt')

for line in file:
    # no esta leyendo el archivo completo, lo leemos linea por linea por lo que no hay bloqueo en memoria
    print(line)

file.close()

# luego de trabajar con el archivo siempre lo debemos cerrar, pero hay una funcion que lo abre y al terminar de ejecutar
# las instrucciones lo cierra, y eso es con with

with open('./text.txt') as file:
    for line in file:
        print(line)

# es la forma mas normal de abrir archivos con py sin tener que preocuparnos si abrir o cerrar el archivo.

