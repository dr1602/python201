nombres = ['Maria', 'Chichen', 'Kukulkan', 'Erendira']
edades = [6, 12, 24, 48]

new_dict_v2 = { nombres[i]:edades[i] for i in range(len(nombres))}
print(new_dict_v2)

new_dict_v3 = dict(zip(nombres,edades))
print(new_dict_v3)

new_dict_v5 = { nombres: edades for (nombres, edades) in zip(nombres, edades)}
print(new_dict_v5)