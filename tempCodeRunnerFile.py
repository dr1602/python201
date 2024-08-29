# a partir de una lista
numbers = [0, 2, 4, 4, 8, 8, 16, 16, 32, 64, 128, 256]
set_numbers1 = set(numbers)
set_numbers2 = set(numbers)
print(set_numbers1)

unique_numbers1 = sorted(list(set_numbers1))

unique_numbers2 = list(set_numbers2)
unique_numbers2.sort()

print(unique_numbers1)
# [0, 2, 4, 8, 16, 32, 64, 128, 256]

print(unique_numbers2)