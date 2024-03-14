import random

def jugar():
    usuario = input("Introduzca una de las siguientes opciones: para piedra (pi), tijera (ti), papel(pa):.\n").lower()
    computadora = random.choice(["pi", "pa", "ti"])
    mensaje = F"HAZ ELEGIDO {usuario} Y LA COMPUTADORA HA ELEGIDO {computadora}."
    
    if usuario == computadora:
        return "EMPATE!\n" + mensaje
    if gano_jugador(usuario, computadora):
        return "Ganaste!!\n" + mensaje
    return "PERDISTE"


def gano_jugador(jugador, oponente):
   
    if ((jugador == "pa" and oponente == "pi")
        or (jugador == "ti" and oponente == "pa")
        or (jugador == "pi" and oponente == "ti")):
        return True
    else:
        return False
    

print(jugar())
