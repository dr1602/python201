# que pasa si dentro de main quisieramos usar data, que esta dentro de mian.py , lo podriamos importar

import main

print(main.data)

'''
al ejecutar example.py tambien se hace la ejecucion de mian.py, no solo se obtiene la dta, tambien
se ejecuta todo el otro codigo

con python3 app/example.py

pero este no es el comportamiento deseado ya que noqueremos que todo dentro de main, se ejecute cuando
ejecutamos example.py
'''


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

'''
[{'Country': 'col', 'Population': 300}, {'Country': 'bol', 'Population': 300}, {'Country': 'arg', 'Population': 400}]
['col', 'bol', 'per', 'mex'] [300, 400, 500, 1000]
[{'Country': 'col', 'Population': 300}]
Ingrese el nombre del pais del que quiere conocer su poblacion:

se controla la ejecucion de mian .py
'''