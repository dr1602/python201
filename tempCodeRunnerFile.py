def multiply_numbers(numbers):
    # Escribe tu solución 👇
    numbers_times2 = list(map(lambda i: i * 2, numbers))
    
    return numbers_times2

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)