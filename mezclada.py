from juego import Game
from random import randrange, shuffle
from jugador import Player

class PalabrasMezcladas(Game):
    def __init__(self, info, player):
        super().__init__(info, player)
        self.penalizacion = 0.5

    def opciones(self):
        opciones = self.questions
        opcion = randrange(len(opciones))
        respuestas = opciones[opcion]
        question = respuestas['question']
        category = respuestas['category']
        words = respuestas['words']

        return words, category, question

    def mostrar_palabras(self, palabras):
        for i, p in enumerate(palabras):
            print(f'{i + 1}. {p}')

    def play_game(self):
        self.mostrar_reglas()
        words, category, question = self.opciones()

        palabras = [list(x) for x in words]

        for x in palabras:
            shuffle(x)

        palabras = [''.join(x) for x in palabras]  

        # Lista de palabras ya encontradas
        listas = []
        print(question)
        # Mientras no se hayan encontrado todas las palabras
        while len(listas) < len(words):
            check = False
            print()
            print('Categoria: ', category)
            self.mostrar_palabras(palabras)
            guess = input('Ingresa palabra ordenada: ').lower()
            if guess == 'exit':
                return False
            elif guess == 'clue':
                print('No hay pistas')
            else:

                for i in range(len(words)):
                    if words[i] == guess and guess not in listas:
                        palabras[i] = words[i]
                        listas.append(palabras[i])
                        check = True
                        continue

                if not check:
                    self.penalizar()

        if len(listas) == len(words):
            return self.ganador()   
            
   

