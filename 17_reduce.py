#  reduce algo a un solo valor, toma una lista y saca una conclusion de una lista
import functools

numbers = [1, 2, 4, 8]

def accum(counter, item):
    print('counter =>', counter)
    print('item =>', item)
    return counter + item

result = functools.reduce(lambda counter, item: counter + item, numbers)

result_v2 = functools.reduce(accum, numbers)

print(result)
print(result_v2)

