from juego import Game
from jugador import Player
from sympy import Symbol, diff, sin, cos, tan, lambdify
from random import randrange
from math import pi

class PregMate(Game):
    def __init__(self, info, player):
        super().__init__(info, player)
        self.penalizacion = 0.25

    def opciones(self):
        opciones = self.questions
        opcion = randrange(len(opciones))
        respuestas = opciones[opcion]
        pregunta = respuestas['question']
        # Sacar la funcion a evaluar
        test = pregunta.split('=')
        test = test[1]

        # Saco el numero a evaluar (los strings son diferentes)
        # hacer el split con f(x), agarrar el primer string, hacerle split en ' ' y agarrar el ultimo item?
        s = pregunta.split(' ')
        try:
            evaluar = eval(s[8])
        except:
            evaluar = eval(s[7])

        return pregunta, test, evaluar

    def play_game(self):
        self.mostrar_reglas()
        pregunta, test, evaluar = self.opciones()
        # Cambio sen por sin porque la libbreria no lee sen
        formula = test.replace('sen', 'sin')

        x = Symbol('x')
        # Convierto la fromula en codigo
        f = eval(formula)
        f_prima = f.diff(x)

        # Uso sympy para evaluar la pregunta y comparar con el resultado iingresado, intente fracciones pero no me comparaba bien el input
        f_prima = lambdify(x, f_prima)
        num = f_prima(evaluar)
        num = str(round(num, 2))
        print(pregunta)
        answer = input('Ingresa la derivada evaluada en pi \n==> ')
        answer = answer.replace(',','.')
        if answer == num:
            return self.ganador()   
        else:
            print('Eso no esta bien')
            self.penalizar()
            return False
