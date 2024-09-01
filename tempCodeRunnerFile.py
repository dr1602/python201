
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)