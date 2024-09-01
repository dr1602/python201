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