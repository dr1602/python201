
increment_v2 = lambda x: x + 1
high_order_function_v2 = lambda x, func: x + func(x)

result = high_order_function_v2(2, increment_v2)
print(result)

result = high_order_function_v2(3, lambda x: x * 2)
print(result)
