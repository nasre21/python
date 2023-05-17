import random


def adivina_el_numero(x):

    print("===============")
    print("Bienvenido al juego")
    print("===============")
    print("Your computer is guess ")


    numero_aleatorio = random.randint(1, x) # Número aleatorio entre 1 y x. 

    prediccion_black = 0
    
    while prediccion_black != numero_aleatorio:
    
        prediccion_black = int(input(f"Adivina numero entre 1 y {x}:")) #f-string

        if prediccion_black < numero_aleatorio:
                    print("intenta otra vez")
        elif prediccion_black > numero_aleatorio:
               print("no intentas")

    print(f"Felicitaciones Advinaste el{numero_aleatorio} corectamente")


adivina_el_numero(10)