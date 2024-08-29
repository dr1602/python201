new_numbers = []

for i in range(1, 11):
    if i % 2 == 0:
        new_numbers.append(i * 2)
    
print(new_numbers)

new_numbers_v1 = [i * 2 for i in range(1,21) if i % 2 == 0]
print(new_numbers_v1)