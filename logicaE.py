from juego import Game
from random import randrange
from jugador import Player

class LogicaE(Game):
    def __init__(self, info, player):
        super().__init__(info, player)
        self.penalizacion = 1

    def opciones(self):
        opciones = self.questions
        opcion = randrange(len(opciones))
        pregunta = opciones[opcion]

        if opcion == 0:
            answer = '67'
        elif opcion == 1:
            answer = '41'
            
        return pregunta, answer

    def play_game(self):
        self.mostrar_reglas()
        pregunta, answer = self.opciones()
        print(self.rules)
        print('\n', pregunta)
        while True:
            respuesta = input('Introduza su respuesta: ')

            if respuesta == answer:
                self.penalizar()
                return self.ganador()


            elif respuesta.lower() == 'exit':
                self.penalizar()
                return False

            elif respuesta.lower() == 'clue':
                print('No hay pistas')

            else:
                self.penalizar()
                return False

