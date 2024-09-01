text = 'Hola, soy David'
vocales = { c: text.count(c) for c in text if c in 'aeiou' }
print(vocales)