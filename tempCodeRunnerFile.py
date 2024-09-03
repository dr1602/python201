try:
    print(0/0)
    assert 1 != 1, 'Uno es igual que uno'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except ZeroDivisionError or AssertionError or Exception as error:
    print(error)

print('hola nuevamente')