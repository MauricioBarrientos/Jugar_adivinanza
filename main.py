import random

def jugar_adivinanza():
    numero_secreto = random.randint(1,100) #genera un numero aleatorio entre 1 y 100
    intentos = 0

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un numero entre 1 y 100. ¡Adivina cuál es!")

    while True:
        intento = int(input("Ingresa tu número: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. ¡Intenta otra vez!")
        elif intento > numero_secreto:
            print("Demasiado alto. ¡Intenta otra vez!")
        else:
            print(f"¡Felicitaciones! Adivinaste el numero en {intentos} intentos.")
            break
    print("Gracias por jugar")

jugar_adivinanza()







