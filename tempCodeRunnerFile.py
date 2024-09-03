
age = 10

if age < 18:
    # vamos a lanzar una excepcion, un error como el de python pero que hacemos y que cumple con las reglas de negocio como no tener menores de edad.
    # para avantar error usamos la palabra reservada raise y excepcion
    raise Exception('No se permiten menores de edad')