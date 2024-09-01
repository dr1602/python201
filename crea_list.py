numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇

even_numbers_v2 = [ number for number in numbers if number % 2 == 0 ]

print('v2 =>', even_numbers_v2)

# lists vs tuples vs set

'''
List: mutable, ordenada, index/slicing, duplicar elementos

tuple: ordenada, index/slicing, duplicar elementos
en sus cados de uso puede servir que la tupla no sea ordenada

tuple: mutable
puede servir para eliminar duplicados
'''