# nuevo tipos de funciones con mayor versatilidad al declarar y tambien al menejrar cierta sintaxis para las funciones

def increment(x):
    return x + 1

increment_v2 = lambda x : x + 1

result = increment(2)
print(result)

result_v2 = increment_v2(2)
print(result_v2)

# nueva forma de uso

full_name = lambda name, last_name: f'The full name is {name.title()} {last_name.title()}'

text = full_name('Rihanna', 'Velazquez')
print(text)