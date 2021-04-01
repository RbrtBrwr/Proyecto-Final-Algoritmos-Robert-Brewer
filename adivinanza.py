from juego import Game
from random import randrange
from jugador import Player

class Adivinanza(Game):
    def __init__(self, info, player):
        super().__init__(info, player)
        self.penalizacion = 0.5

    def opciones(self):
        opciones = self.questions
        opcion = randrange(len(opciones))
        # Clues
        datos = opciones[opcion]
        pregunta = datos['question']
        respuestas = datos['answers']
        clues = [datos['clue_1'],datos['clue_2'],datos['clue_3']]

        return pregunta, respuestas, clues


    def play_game(self):
        self.mostrar_reglas()

        pregunta, respuestas, clues = self.opciones()
        # Para saber que pista mostrar
        clue_num = 0

        while True:
            print(f'Pregunta: {pregunta}')
            respuesta = input('==> ')
            if respuesta.lower() == 'exit':
                return False
            elif respuesta.lower() == 'clue':
                # Muestra la pista correspondiente si el usuario tiene mas pisatas
                if self.player.pistas > 0:
                    if self.mostrar_pista(clues, clue_num):
                        self.player.pistas -= 1
                        clue_num += 1
                    else:
                        print('No tienes mas pistas')
                    
            elif respuesta in respuestas:
                return self.ganador()
            else:
                print(self.penalizar())
                return False
