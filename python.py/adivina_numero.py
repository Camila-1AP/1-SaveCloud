# Adivina el numero que la maquina elija
# ALGORITMO:
# bienvenida al juego
# explicacion del jurego
# importar modulo ramdom
# indicar el rango de numeros que utilizara
# crear statements de las probabilidades de respuesta del ususario

print("==================================")
print("     BIENVENIDO/A AL JUEGO        ")
print("==================================")
print("==================================")
print("LA EXPLICACION DEL JUEGO ES LA SIGUIENTE:")
print("La maquina elijira un numero random y tendras que adivinar con las pistas que se muestren.")
print("==========================")
print("   QUE EMPIECE EL JUEGO!  ")

import random

def adiv_random(w):
    maq = random.randint(0, w)
    prediccion = 0
    while prediccion != maq:
        prediccion = int(input(F"Introduzca un nemero entre 0 y {w}: "))
        if  prediccion > maq:
            print("Intente con un numero MENOR: ")
        elif prediccion < maq:
            print("Intente con un numero MAYOR: ")

    print("++++++++++++++++++++++++++++++++++++")
    print("  FELICIDADES HAZ GANADO EL JUEGO!! ")
    print("++++++++++++++++++++++++++++++++++++")
    print(F"EL NUMERO ADIVINADO ES: {maq} ")


adiv_random(21)