from juego import Game
from random import randrange
from jugador import Player

class EscogeNumero(Game):
    def __init__(self, info, player):
        super().__init__(info, player)
        self.penalizacion = 0.25


    def high_low(self, num, number):
        # Dice si el numero ingresado esta arriba o abajo del que es
        test = number - num

        if number - num > 10:
            print('demasiado alto')
        elif number - num > 7:
            print('muy alto')
        elif number - num > 3:
            print('alto')
        elif number - num > 0:
            print('un poquito mas abajo')
        elif number - num < -10:
            print('demasiado bajo')
        elif number - num < -7:
            print('muy bajo')
        elif number - num < -3:
            print('bajo')
        elif number - num < 0:
            print('un poquito mas arriba')

        
            
            
            
    
    def play_game(self):
        self.mostrar_reglas()
        # Escoje el numero entre 1 y 15
        num = randrange(1,16)

        x = 0
        win = False

        # El jugador tiene tres intentos
        while x < 3:
            number = input('Escoge un numero entre 1 y 15: ')
            if number.lower() == 'exit':
                return False
            elif number.lower() == 'clue':
                print('No hay pistas')
            elif not number.isnumeric():
                print('Ingresa solo numeros')
            else:
                number = int(number)
                if number == num:
                    win = True
                    break
                
                else:
                    x += 1
                    self.high_low(num, number)


        if win:
            return self.ganador()
        else:
            # Un cuarto de vida menos
            self.penalizar()
            return False
