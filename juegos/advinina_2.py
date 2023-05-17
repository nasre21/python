import random


def maestro(x):
    print("========================")
    print("bienvenido")
    print(f"Selecciona un numero entre 1 y {x} para que la computadora")


    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior
        respuesta = input(f"Mi preddicion es {prediccion}. Si es muy baja, ingresa(A). Si es muy alta, ingresa(B).Si es media, ingresa(C)").lower()


        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"Thank you: {prediccion}")


maestro(10)