from juego import Game
from random import randrange, shuffle
from time import time
from jugador import Player

class Quizizz(Game):
    def __init__(self, info, player):
        super().__init__(info, player)



    def opciones(self):
        opciones = self.questions
        opcion = randrange(len(opciones))
        respuestas = opciones[opcion]
        pregunta = respuestas['question']
        respuesta_correcta = respuestas['correct_answer']
        clue = [respuestas['clue_1']]


        opciones = []
        for key, value in respuestas.items():
            if key in ['correct_answer', 'answer_2', 'answer_3', 'answer_4']:
                opciones.append(value)

        return pregunta, respuesta_correcta, opciones, clue

    def play_game(self):
        self.mostrar_reglas()
        pregunta, respuesta_correcta, opciones, clue = self.opciones()

        posiciones = [0,1,2,3]
        shuffle(posiciones)
        clue_num = 0

        start = time()

        i = 0
        while (time() - start) < 60: 
            print(pregunta)
            win = False
            keys = ['A','B','C','D']
            for i in range(4):
                print(f'{keys[i]} {opciones[posiciones[i]]}')

            seleccion = input('Ingrese la letra de la opcion que considera correcta\n==> ').upper()
            if seleccion == 'EXIT':
                return False
            elif seleccion == 'CLUE':
                self.mostrar_pista(clue, clue_num)
                
            elif seleccion == 'A':
                if opciones[posiciones[0]] == respuesta_correcta:
                    if (time() - start) < 60:
                        return self.ganador()

                    else:
                        print('Se te acabo el tiempo')
                        self.penalizar()
                        return False
                else:
                    print('perdiste')
                    self.penalizar()
                    return False

            elif seleccion == 'B':
                if opciones[posiciones[1]] == respuesta_correcta:
                    if (time() - start) < 60:
                        return self.ganador()
                    else:
                        print('Se te acabo el tiempo')
                        self.penalizar()
                        return False

                else:
                    print('perdiste')
                    self.penalizar()
                    return False

            elif seleccion == 'C':
                if opciones[posiciones[2]] == respuesta_correcta:
                    if (time() - start) < 60:
                        return self.ganador()
                    else:
                        print('Se te acabo el tiempo')
                        self.penalizar()
                        return False
                else:
                    print('perdiste')
                    self.penalizar()
                    return False

            elif seleccion == 'D':
                if opciones[posiciones[3]] == respuesta_correcta:
                    if (time() - start) < 60:
                        return self.ganador()
                    else:
                        print('Se te acabo el tiempo')
                        self.penalizar()
                        return False
                else:
                    print('perdiste')
                    self.penalizar()
                    return False
            else: 
                print('Opcion invalida')
