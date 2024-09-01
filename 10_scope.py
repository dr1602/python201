# creamos una variable, hasta donde esas variables tienen un alcance para poder trabajar

'''
existen el scope (de mayor a menor):
a. Built-in
b. Global scope
c. Enclosing scope
d. Local scope

'''

price = 100 # alcance global

def increment():
    price = 200
    # aqui estas una nueva variable dentro del contexto que se llama price 
    price = price + 10
    # pero ahora price tiene un contexto local
    print(price)
    print(f'aqui esta almacenado el price local {id(price)}')
    return price
    

print(price)
print(f'esto es donde esta almacenado el price global {id(price)}')

price_2 = increment()
print(price_2)

# funcion sin contexto definido

price = 100 # alcance global
result = 200

def increment():
    price = 200
    # aqui estas una nueva variable dentro del contexto que se llama price 
    price = price + 10
    # pero ahora price tiene un contexto local
    print(price)
    return price
    

print(price)
price_2 = increment()
print(price_2)
print(result)

''' explicado con espacios de la memoria'''

price = 100 # alcance global

def increment():
    # aqui estas una nueva variable dentro del contexto que se llama price 
    price = 10
    # pero ahora price tiene un contexto local
    print(price)
    print(f'aqui esta almacenado el price local {id(price)}')
    

print(price)
print(f'esto es donde esta almacenado el price global {id(price)}')

increment()




