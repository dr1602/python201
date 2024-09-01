# bloques de codigo que se ejecutan multi[les veces encaspulados en algo llamado funcion]
# con esto ganamos mantenibilidad

# FUNCTIONS

# funcion print que recibe un argumento que imprime en termina
print('Hola')

# haremos nuestra propia funcion de impresion

def my_print(text):
    print(text * 2)
    print('This is my print 2')
    
my_print('Perrito')
my_print('Let`s dance')

a = 10
b = 90

c = a + b

print(c)

def suma(a, b):
    # tiene esta funcion dos repsonsabilidades
    # una es sumar
    # la otra es imprimir
    print( a + b)
    
suma(12,14)
suma(10, 5)

# podemos reusar funcoines dentro de funciones

def suma(a, b):
    # tiene esta funcion dos repsonsabilidades
    # una es sumar
    # la otra es imprimir
    my_print( a + b)
    
suma(12,14)
suma(10, 5)

