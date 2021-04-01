from juego import Game
from random import randrange, choice
from string import ascii_uppercase
from jugador import Player

class Sopita(Game):
    def __init__(self, info, player):
        super().__init__(info, player)
        self.penalizacion = 0.5




    def opciones(self):
        opciones = self.questions
        opcion = randrange(len(opciones))
        respuestas = opciones[opcion]
        words = []
        clues = []

        for key, value in respuestas.items():
            if key == 'answer_1' or key == 'answer_2' or key == 'answer_3':
                words.append(value.upper())
            elif key == 'clue_1' or key == 'clue_2' or key == 'clue_3':
                clues.append(value)

        return words, clues
                
        

    def placement(self, words):
        # Posibles posiciones para las palabras 
        posiciones = ['diagonal', 'vertical', 'horizontal']

        unavailable = []
        palabras = {}
        for word in words:
            
            palabras[word] = []
            vector = []
            # Par probar que la posicion no este usada por otra palabra
            posicion = choice(posiciones)
            if posicion == 'diagonal':
                step_x = 1
                step_y = 1
                start_x = choice(range(15 - len(word)))
                start_y = choice(range(15 - len(word)))
            elif posicion == 'horizontal':
                step_x = 1
                step_y = 0
                start_x = choice(range(15 - len(word)))
                start_y = choice(range(15))
            else:
                step_x = 0
                step_y = 1
                start_y = choice(range(15 - len(word)))
                start_x = choice(range(15))

            for j in range(len(word)):
                pos = (start_y, start_x)
                vector.append(pos)
                start_x += step_x
                start_y += step_y
                
                # Si no se pueden esas posiciones, vuelve a llamar la funcion
                if pos in unavailable:
                    return self.placement(words)
                
                else:
                    unavailable.append(pos)
                    palabras[word].append(pos)
        
        return palabras

    def set_words(self, palabras, grid):
        for k, coords in palabras.items():
            for i in range(len(k)):
                grid[coords[i][0]][coords[i][1]] = k[i]

    def print_grid(self, grid):
        # Generar grid
        grid_size = len(grid)

        for y in range(grid_size):
            for x in range(grid_size):
                print(grid[y][x], end=" ")
            print()

    def play_game(self):
        self.mostrar_reglas()
        grid_size = 15
        grid = [[choice(ascii_uppercase) for x in range(grid_size)] for y in range(grid_size)]
        clue_num = 0

        words, clues = self.opciones()

        lose = 0
        palabras = self.placement(words)
        check = []

        while len(check) != len(words):
            if lose >= 3:
                print('Perdiste :(s')
                return False

            self.set_words(palabras, grid)
            self.print_grid(grid)
            test = input('\n==> ').upper()
            if test == 'EXIT':
                return False
            elif test == 'CLUE':
                self.mostrar_pista(clues, clue_num)
            
            # Si la palabra esta entre las buscadas
            elif test in words:
                # Si ya encontraste la palabra
                if test in check:
                    print('\npalabra ya encontrada\n')
                else:
                    check.append(test)
            else:
                print('\nPalabra incorrecta, media vida menos\n')
                self.penalizar()
                lose += 1

        
        return self.ganador()
    
