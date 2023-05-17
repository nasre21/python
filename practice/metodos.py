my_dict = {'a': 1, 'b': 2, 'c': 3}

# Usando el método 'keys()' para imprimir todas las claves del diccionario
print(my_dict.keys()) # salida: dict_keys(['a', 'b', 'c'])

# Usando el método 'values()' para imprimir todos los valores del diccionario
print(my_dict.values()) # salida: dict_values([1, 2, 3])

# Usando el método 'items()' para imprimir todas las parejas clave-valor del diccionario
print(my_dict.items()) # salida: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Usando el método 'get()' para obtener el valor de una clave específica
value = my_dict.get('a')
print(value) # salida: 1

# Usando el método 'pop()' para eliminar una clave específica del diccionario
my_dict.pop('a')
print(my_dict) # salida: {'b': 2, 'c': 3}
