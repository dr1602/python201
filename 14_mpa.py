# utilizar hof y lambda en funciones directamente construidas en python como map
# map hace trasnformacion a una lista dada de elementos, estas funcoines te dan bajo las listas

numbers = [1, 2, 3, 4, 5, 6]
numbers_v2 = []

for number in numbers:
    numbers_v2.append(number * 2)
    
print(numbers)
print(numbers_v2)

# podemos hacer esa misma funcion en una sola linea y con lambda functions

# esto lo manda directamente como un iterable
# numbers_v3 = map(lambda i: i * 2, numbers)

numbers_v3 = list(map(lambda i: i * 2, numbers))
# no es necesario crear un nuevo array para guardar los valores

print(numbers_v3)

# nuevo ejercicio

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)

# utiliza como referencia a la lista mas pequena
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)

# nota adicional, lo mas comun no es tener una lista con valores primitivos sino con diccionarios
# lo veremos en la siguiente clase