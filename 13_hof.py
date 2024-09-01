# funcoines de order superior o high order function, en sus siglas HOF, es importante
# a una funcion le podemos mandar otra funcion y ejecutarla desde ahi
# tambien podemso mandar como un atributo una funcion y ejecutarla dentro de la funcion

def increment(x):
    return x + 1

def high_order_function(x, func):
    # aqui se ejecuta la funcion
    return x + func(x)

# aqui no se necesita ejecutar la funcion, solo se necesita la definicion de la funcion, porque adentro se va a ejecutar
result = high_order_function(2, increment)

# 2 +  (2 + 1)
print(result)

# beneficios es poder usar lambdas o funciones sin usar toda la estructura

## ejemplo con lambdas

increment_v2 = lambda x: x + 1
high_order_function_v2 = lambda x, func: x + func(x)

result = high_order_function_v2(2, increment_v2)
print(result)

result = high_order_function_v2(3, lambda x: x * 2)
print(result)
