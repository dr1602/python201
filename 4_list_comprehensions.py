# empezaremos la lista con los corchetes cuadrados, primero la estructura sera
# [element for element in iterable]

# forma clasica
numbers = []

for element in range(1, 11):
    numbers.append(element * 2)
    
print(numbers)
'''
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''

# forma simiplificada
# sintaxis mas corta, y facil de leer
numbers_v1 = [element for element in range(1,21)]
print(numbers_v1)
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''

# otra forma de trabajar con la version simplificada
numbers_v2 = [element * 2 for element in range(1,21)]
print(numbers_v2)
'''
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
'''

# nueva forma de la sitnaxis para agregar condiciones
# [element for element in iterable if condicion]

# [i*2 for i in rnage(1, 101) if i % 2 == 0]

new_numbers = []

for i in range(1, 11):
    if i % 2 == 0:
        new_numbers.append(i * 2)
    
print(new_numbers)
'''
[4, 8, 12, 16, 20]
'''

new_numbers_v1 = [i * 2 for i in range(1,21) if i % 2 == 0]
print(new_numbers_v1)
'''
[4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
'''


