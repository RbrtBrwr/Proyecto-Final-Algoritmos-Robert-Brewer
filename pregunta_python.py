from juego import Game
from random import randrange
from jugador import Player
from time import sleep

class PreguntaPython(Game):
    '''
    solucion1 = int(''.join([w for w in [y.replace(",00","") for y in [x for x in frase.split()]] if w.isnumeric()]))

    solucion2 = " ".join([x[::-1] for x in frase.split()])
    '''
    def __init__(self, info, player):
        super().__init__(info, player)
        self.penalizacion = 0.5


    def opciones(self):
        opciones = self.questions
        opcion = randrange(len(opciones))
        seleccion = opciones[opcion]
        pregunta = opciones[opcion]['question']
        clues = []

        for key, value in seleccion.items():
            if key == 'question':
                pregunta = value
            elif key == 'clue_1' or key == 'clue_2' or key == 'clue_3':
                clues.append(value)
            else:
                answer = value

        return pregunta, clues, answer, opcion
        
    def play_game(self):
        self.mostrar_reglas()
        pregunta, clues, respuesta, opcion = self.opciones()
        print(pregunta)
        # Extra el substring del string
        frase = pregunta.split('"')[1]
        clue_num = 0

        # Respuestas para cada opcion
        if respuesta == 'string invertido':
            answer = frase.split()
            for i in range(len(answer)):
                answer[i] = answer[i][::-1]

            answer = ' '.join(answer)

        else:
            answer = 50

        while True:    
            quedice = input('Ingrese el codigo en una sola linea\n==> ')
            if quedice == 'exit':
                return False
            elif quedice == 'clue':
                self.mostrar_pista(clues, clue_num)
            else:
                # Convierte user input a codigo
                test = eval(quedice)

                if test == answer:
                    print(answer)
                    sleep(2)
                    return self.ganador()
                    
                else:
                    self.penalizar()
                    return False



# game_python = {
#     "message_requirement": "mi pantalla no funciona",
#     "requirement": "cable HDMI",
#     "name": "Preguntas sobre python",
#     "rules": "pierde media vida por cada prueba incorrecta",
#     "award": "carnet",
#     "questions": [
#     {
#     "question": "Tengo el siguiente string: frase  = \"tengo en mi cuenta 50,00 $\". Escribe en una línea de código como extraer de este string los 50 en formato entero",
#     "answer": "Validar en python que de el siguiente resultado: 50.00 en formato entero",
#     "clue_1": "utiliza replace",
#     "clue_2": "utiliza split",
#     "clue_3": "utiliza int"
#     },
#     {
#     "question": "Invierte este string con python en un línea  para poder leerlo frase = \"oidutse ne al ortem aireinegni ed sametsis\"",
#     "answer": "string invertido",
#     "clue_1": "utiliza slices"
#     }
#     ]
#     }