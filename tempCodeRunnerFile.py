def my_divide(a, b):
    # Escribe tu solución 👇
    result = 0
    try:
        result = a / b
    except ZeroDivisionError or AssertionError:
       result = print('No se puede dividir por 0')

    return result
    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0