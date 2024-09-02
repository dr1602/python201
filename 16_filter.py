# con filter vamos a seleccionar ciertos elementos de un lista, para que pertenezcan a una nueva lista.
# una nueva lisa con los elementos que cumplen esa condicion
# nunca se obtendra una lista con mas elementos de los que se setearon originalmente

numbers = [1, 2, 3, 4, 5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# como es una lista de numeros no hay problema con la referencia de memoria

print(new_numbers)
print(numbers)