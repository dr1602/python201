# como modificar conjuntos
# agregar, remover, etc.

set_countries = {'México', 'Colombia', 'Bolivia', 'El Salvador', 'Guatemala', 'México', 'México', 'Honduras', 'Nicaragua', 'Brasil' }

# podemos preguntar el tamaño

size = len(set_countries)
print(size)

print('Colombia' in set_countries)
print('Brasil' in set_countries)

# add
set_countries.add('Suriname')
print(set_countries)

set_countries.add('Suriname')
print(sorted(set_countries))

# update
# funciona similar a agregar pero los elementos del conjunto pequeno los agregara a set_countries
set_countries.update({ 'Argentina', 'Suriname', 'Ecuador' })
print(sorted(set_countries))

# remove
set_countries.remove('El Salvador')
print(sorted(set_countries))

# solo puedes eliminar un elemento a la vez
# set_countries.remove(('Argentina', 'Bolivia'))

set_countries.remove('Argentina')
set_countries.remove('Bolivia')
print(sorted(set_countries))

# no elimina no coincidencias
# set_countries.remove('Meshico')

# una forma de no estallar si no existe es:
set_countries.discard('Meshico')
print(sorted(set_countries))

# para limpiar todo el conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries))
