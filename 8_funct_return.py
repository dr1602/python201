## las funcoines reciben parametros y deberian retornar la respuesata de la suma
# para poder usarlo

def sum_with_range(min, max):
    print(min, max)
    
    sum = 0
    for  x in range(min, max):
        sum += x
    
    return sum    

# asignamos el valor del resultado a una variable y por eso depsues lo podimos imprimir
result = sum_with_range(1, 10)
print(result)

result_2= sum_with_range(result, result + 10)
print(result_2)
