# tomar una palabra
# con f-string, la combina con un texto predeterminado

# ALGORITMO
# Bienvenida al juego
# input, verbo, adjetivo, sustantivo
# formar el f-string
# indicar que su "historia loca" es la siguiente

print("-----------------------------")
print("   BIENVENIDO/A AL JUEGO!!   ")
print("-----------------------------")

adjetivo = input("Introzca un adjetivo: ")
sustantivo = input("introduzca un sustantivo: ")
verbo = input("Introduzca un verbo: ")

print("SEGUN SUS DATOS SU HISTORIA SE VE ASI:")

print(f"Me {adjetivo} {verbo} porque es maravillo y siempre eso es {sustantivo}.")