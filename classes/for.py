contador = 0
mi_email = input("intruduce your gmail:")

for i in mi_email:

    if i == "@" or i == ".":
        contador = contador + 1

if contador == 2:
    print("email es correcto")

else:
    print("el email no es correcto")