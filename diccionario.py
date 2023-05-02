 # Diccionario
mis_objetos = {"black01":True,"black02":2,"black03":"nasser","black04":4,"black05":5}

print(mis_objetos["black01"])

# El resultado (True)

valor1 = mis_objetos.get("black02")

print(valor1)
# Resultado (2)


frutas_vitamina_c = {
    "naranja": 50,
    "limón": 40,
    "kiwi": 90,
    "fresa": 60,
    "papaya": 30
}
print(len(frutas_vitamina_c))  # Imprime la cantidad de elementos del diccionario
print("naranja" in frutas_vitamina_c)  # Imprime True si la clave "naranja" está en el diccionario
