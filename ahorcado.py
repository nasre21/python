import random
import string

from palabras import palabras
from digramas import vidas_diccionario_visual

def obtener(palabras):

        palabra = random.choice(palabras)

        while "-" in palabra or " " in palabras:
              palabra = random.choice(palabras)
        
        return palabra.upper()

def ahorcado():
    print("=================================")
    print("Bienvenido al juego")
    print("=================================")

    palabra = obtener(palabras)

    letras_red=  set(palabra)
    letras_black=  set()
    letras_white=  set(string.ascii_uppercase)

    vidas = 7

    while len(letras_red) > 0 and vidas > 0:
          print(f"Te quedam {vidas} vidas y has estas letras: {' '.join(letras_black)}")

          palabra_lista = [letra if letra in letras_black else '-' for letra in palabra]
          print(vidas_diccionario_visual[vidas])
          print(f"Palabra: {' '.join(palabra_lista)}")

          letra_user = input("Escoge una letra: ").upper()

          if letra_user in letras_white - letras_black:
                letras_black.add(letra_user)
                
                if letra_user in letras_red:
                      letras_red.remove(letra_user)
                      print('')
                else:
                      vidas = vidas - 1
                      print(f"\nla letra {letra_user} no esta en la palabra")

          elif letra_user in letras_black:
                print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")

          else: 
                print("\nNo serve")
    

          if vidas == 0:
                print(vidas_diccionario_visual[vidas])
                print(f"Ahorcado èrdiste. Lo lamento. La palabra era: {palabra}")
          else:
                print(f"Exlente {palabra}")


ahorcado() 
