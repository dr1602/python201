def message_creator(text):
    # Escribe tu solución 👇
    test = str(text)
    answer = str
    if test == 'computadora':
       answer = 'Con mi computadora puedo programar usando Python'
    elif test == 'celular':
        answer = 'En mi celular puedo aprender usando la app de Platzi'
    elif test == 'cable':
        answer = '¡Hay un cable en mi bota!'
    else:
        answer = 'Artículo no encontrado'
       
    return answer

text = 'computadora'
response = message_creator(text)
print(response)