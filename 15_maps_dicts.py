# podemos hacer transformaciones no convencionales, como pasar de comida a carros
# cambiando el tipo de datos

items = (
    # lista de diccionario
    {
        'product': 'camisa',
        'price': 100,
    },
        {
        'product': 'pantalon',
        'price': 120,
    },
    {
        'product': 'zapatos',
        'price': 90,
    },
)

# vamos a transformar a lista de nuemerso, en este caso solo de precios

prices = list(map(lambda item: item['price'], items))

# el array esta en su estado original
print(items)

# transfromamos a una lista con el mismo numero de elementos pero ahora de diccionario a enteros puros
print(prices)

# nuevo atributo al array, en este caso los impuestos y agregarlo en la orden de compra
# usaremos un map para transformar el diccionario dentro de la lista, agregando un nuevo atributo

# un tema a considerar es que las lambdas se hace en una sola lista
# new_items = list(map(lambda ))

def add_taxes(item):
    item['taxes'] = item['price'] * .16
    return item

new_items = list(map(add_taxes, items))
print(new_items)

# aqui si se modifica el array porque hay trabaja que involucra llamado al espacio en memoria que se vera mas tarde
print(items)

# hay que tener precaucion en este tipo de modificaciones
# el map no modifica el array original sino que genera uno nuevo

# al trabajar con diccionarios al modificar un atributo, edue que modifiques todo el original y no 
# y no generando uno nuevo lo que puede generar problemas si no es lo que esperas
# como solucionarias este problema?
# como se peude hacer que el original se respete?

