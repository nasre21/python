import random


def play():
    user = input("Escogeun opcion: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
    computer = random.choice(['pi', 'pa', 'ti'])

    if user == computer:
        return "Empate"
    
    if ganar(user, computer):
        return "ganar"
    
    return "perdir"


def ganar(jugador, oponente):

    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False
    

print(play())