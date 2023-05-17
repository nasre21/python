mi_diccionario = {"name": "nasser", "apellido":"oufallah","pais":"Mar"}
mi_diccionario["Italia"]= "Lisboa"
print(mi_diccionario)
mi_diccionario["Italia"]= "Roma"
print(mi_diccionario)
del mi_diccionario["name"]
print(mi_diccionario)

mi_tupla = ["España", "Francia", "Reino Unido"]
mi_diccionario2 = {mi_tupla[0]:"Madrid", mi_tupla[1]:"Paris", mi_tupla[2]:"London"}
print(mi_diccionario2["Francia"])

mi_diccionario3 = {23:"Jordan", "nombre": "Micheal", "Equipo":"Chicago", "anillos":{"temporadas":[1992,1993,1994,1995]}}
print(mi_diccionario3.keys())
print(mi_diccionario3.values())
print(len(mi_diccionario3))
print(mi_diccionario3["anillos"])
