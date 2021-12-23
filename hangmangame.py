import random
import string

from words import palabras
from visual import vidas_visual


def obtener_palabra(palabra_obtenida):
    palabra_obtenida = random.choice(palabras)
    # Si tiene - o espacio va a seguir seleccionando una palabra al azar
    while '-' in palabra_obtenida or ' ' in palabra_obtenida:
        palabra_obtenida = random.choice(palabras)

    return palabra_obtenida.upper()


def juego():
    print('================================')
    print('Bienvenido \n ')
    print('================================')

    palabra_a_adivinar = obtener_palabra(palabras)

    # Guarda las letras por adivinar en una lista
    letras_por_adivinar = set(palabra_a_adivinar)
    letras_adivinadas = set()  # lista para ir guardando las letras que si adivino
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(
            f"\n Letras usadas : {' '.join(letras_adivinadas)}\n Tus vidas restantes: {vidas}")

        # Lista que muestra el estado de la palabra
        palabra_lista = [letra if letra in letras_adivinadas
                         else '-' for letra in palabra_a_adivinar]

        print(vidas_visual[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input('Escoge una letra: ').upper()

        # Si acierta la palabra se añade a la lista de adivinadas, sino se le resta una vida
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f'\n La letra {letra_usuario} no esta en la palabra.')
        # Si ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print('\n Letra ya escogida, ingrese una nueva.')

        else:
            print('\n Letra no valida.')

    if vidas == 0:
        print(vidas_visual[vidas])
        print(f'\n Juego terminado, la palabra era {palabra_a_adivinar}')
    else:
        print("Ganaste!")


if __name__ == '__main__':
    juego()
