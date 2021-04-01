from juego import Game
from random import randrange
from string import ascii_uppercase
from jugador import Player

class Criptograma(Game):
    def __init__(self, info, player):
        super().__init__(info, player)
        self.penalizacion = 1

    def opciones(self):
        opciones = self.questions
        opcion = randrange(len(opciones))
        mensaje = opciones[opcion]["question"].replace('á', 'a')
        desplazamiento = opciones[opcion]["desplazamiento"]
        return mensaje, desplazamiento

    def inicializar_alfabeto_cifrado(self, desplazamiento, alfabeto):
        # Crea alfabeto cifrado con el desplazamiento
        size = 25
        alfabeto_cifrado = [l for l in alfabeto[-desplazamiento::]]

        nuevo = desplazamiento
        i = 0
        while nuevo <= size:
            alfabeto_cifrado.append(alfabeto[i])
            nuevo += 1
            i += 1

        return alfabeto_cifrado

    def cifrar_mensaje(self, mensaje, alfabeto_cifrado, alfabeto):
        # Encripta mensaje con el alfabeto cifrado
        mensaje_cifrado = []
        for i in mensaje.upper():
            for j in range(len(alfabeto)):
                if alfabeto[j] == i:
                    mensaje_cifrado.append(alfabeto_cifrado[j])
                    continue
        mensaje_cifrado = ''.join(mensaje_cifrado)
        return mensaje_cifrado

    def play_game(self):
        self.mostrar_reglas()

        mensaje, desplazamiento = self.opciones()
        # Inicializa el alfabeto normal
        alfabeto = list(ascii_uppercase)
        size = 25

        # Inicializa alfabeto Cifrado
        alfabeto_cifrado = self.inicializar_alfabeto_cifrado(desplazamiento, alfabeto)

        alfabeto_cifrado.append(' ')
        alfabeto.append(' ')
        print(f'Alfabeto:         ', *alfabeto)
        print(f'Alfabeto Cifrado: ', *alfabeto_cifrado)

        mensaje_cifrado = self.cifrar_mensaje(mensaje, alfabeto_cifrado, alfabeto)

        print('Mensaje Cifrado: ' + mensaje_cifrado)

        while True:
            answer = input("Cual es el mensaje original?\n==> ").upper()
            if answer == 'EXIT':
                return False
            elif answer == 'CLUE':
                print('No hay pistas')
            elif answer == mensaje.upper():
                print("Es correcto! Ganaste!")
                self.availability = False
                return self.ganador()
            else:
                print('Mmmm, ese no es')
                self.penalizar()
                break


