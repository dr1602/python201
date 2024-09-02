import package
print(package.URL)
'''
la url hace parte del paquete

Se inicio paquete
platzi.com
'''

# tambien podemos usarlo para definir un name space, donde los espacios de nombres son itneresantes
# y de veriamos hacer mayor uso de ellos

print(package.mod_1.func_1())

# esto es debil y puede causar errores pero solo sirve porque antes ya importamos esos modulos

'''
Se inicio paquete
platzi.com
Traceback (most recent call last):
  File "/root/Python201/tempCodeRunnerFile.py", line 14, in <module>
    print(package.mod_1.func_1())
AttributeError: module 'package' has no attribute 'mod_1'

genera error porque no hay importacion explicita
'''

# como se puede automatizar para que no se genere error