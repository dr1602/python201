# para manejar listas
import collections

numbers = [1, 2, 1, 2, 2, 1, 5, 7, 7, 8, 9, 5, 6, 13, 15, 21]
counter = collections.Counter(numbers)
print(counter)