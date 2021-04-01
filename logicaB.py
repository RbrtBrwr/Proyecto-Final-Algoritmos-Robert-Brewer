from juego import Game
from random import randrange
from jugador import Player

class LogicaB(Game):
    def __init__(self, info, player):
        super().__init__(info, player)
        self.penalizacion = 0.5

    def opciones(self):
        opciones = self.questions
        opcion = randrange(len(opciones))
        respuestas = opciones[opcion]
        pregunta = respuestas['question']
        answer = respuestas['answer']


        return pregunta, answer

    def play_game(self):
        self.mostrar_reglas()
        question, answer = self.opciones()
        if answer == 'True':
            check = ['t','true','v','verdadero','verdadera']
        else:
            check = ['f','false','falso','falsa']

        print(question)
        while True:
            respuesta = input('==> ').lower()
            if respuesta == 'exit':
                return False
            elif respuesta == 'clue':
                print('No hay pistas')

            elif respuesta in check:
                return self.ganador()
                
            else:
                print("Perdiste :'( ") #)
                self.penalizar()
                return False

