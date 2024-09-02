
import main

# main.run()

# con esto ya controlamos la ejecucion del archivo, no se ejecuta por solo ejecutarlo
# explictamente tenemos que ejecutar la funcion run
# pero si tuvieramos una variable, como la variable dat, fuera del scop de la funcion

# aqui en example podemos imprimir main.data
# no solo por importar va a ejcuttar el archivo, solo deberia imprimir data.

print(main.data)

'''
[{'Country': 'col', 'Population': 300}, {'Country': 'bol', 'Population': 300}, {'Country': 'arg', 'Population': 400}]
'''

main.run()
