from juego import Game
from random import randrange
from jugador import Player
from time import sleep

class Ahorcado(Game):
    def __init__(self, info, player):
        super().__init__(info, player)
        self.penalizacion = 0.25


    def opciones(self):
        # Saca la info del diccionario, cambia un poco de juego en juego
        opciones = self.questions
        opcion = randrange(len(opciones))
        respuestas = opciones[opcion]
        pregunta = respuestas['question']
        respuesta = respuestas['answer']
        clues = [respuestas['clue_1'],respuestas['clue_2'],respuestas['clue_3']]

        return pregunta, respuesta, clues

    def dibujitos_print(self, palabra, x):
        # Imprime el dibujito correspondiente
        palabra = palabra
        dibujitos = {
            1: 
            f'''
            -----
            |   
            |    
            |    
            |
            L____ 

        {palabra}

            ''',
            2: 
            f'''
            -----
            |   |
            |   
            |   
            |
            L____  

        {palabra}

            ''',
            3: 
            f'''
            -----
            |   |
            |   0
            |    
            |
            L____   

        {palabra}

            ''',
            4: 
            f'''
            -----
            |   |
            |   0
            |   | 
            |
            L____ 

        {palabra}

            ''',
            5: 
            f'''
            -----
            |   |
            |   0/
            |  /| 
            |   
            L____ 

        {palabra}

            ''',
            6: 
            f'''
            -----
            |   |
            |   0/
            |  /| 
            |  / \ 
            L____

        {palabra}

            ''',
        }
        print(dibujitos[x])

    def play_game(self):
        self.mostrar_reglas()

        pregunta, answer, clues = self.opciones()
        
        # Numero de pista para mostrar
        clue_num = 0

        # Palabra sin adivinar
        palabra = ['_' for i in answer]
        palabra_nueva = ' '.join(palabra)
        x = 1
        self.dibujitos_print(palabra_nueva, x)

        while True:
            if '_' not in palabra:
                return self.ganador()
            
            print(pregunta)

            while True:
                try:
                    guess = input('Ingrese la letra o palabra que quiere probar: ').lower()
                    if not guess.isalpha():
                        raise Exception

                    break

                except:
                    print('Ingresa solo letras')

            if len(guess) > 1:
                if guess == 'exit':
                    # Salir del juego
                    return False
                elif guess == 'clue':
                    # Muestra pista si el usuario tiene
                    if self.player.pistas > 0:
                        if self.mostrar_pista(clues, clue_num):
                            self.player.pistas -= 1
                            clue_num += 1
                    else:
                        print('No tienes mas pistas')

                elif guess.lower() == answer.lower():
                    # Cuando ingresa una palabra
                    answer = ' '.join(list(answer))
                    self.dibujitos_print(answer, x)
                    return self.ganador()

                else:
                    # Si la palabra ingresada es incorrecta
                    if x < 5:
                        x += 1
                    else:
                        x += 1
                        palabra_nueva = ' '.join(palabra)
                        self.dibujitos_print(palabra_nueva, x)
                        print('Esa no es la palabra')
                        self.penalizar()

                    palabra_nueva = ' '.join(palabra)
                    self.dibujitos_print(palabra_nueva, x)

            else:
                if guess not in answer and guess.upper() not in answer:
                    # Cambia el dibujito por letra incrrecta y penaliza
                    if x < 5:
                        x += 1
                        print('Incorrecto')
                        self.penalizar()
                    else:
                        x += 1
                        palabra_nueva = ' '.join(palabra)
                        self.dibujitos_print(palabra_nueva, x)
                        print('Incorrecto')
                        self.penalizar()
                        sleep(3)
                        return False

                    palabra_nueva = ' '.join(palabra)
                else:   
                    # Cambia uno de los espacios a la letra elejida    #  
                    for i in range(len(answer)):
                        if answer[i].lower() == guess:
                            palabra[i] = answer[i]

                    palabra_nueva = ' '.join(palabra)
                
                self.dibujitos_print(palabra_nueva, x)


