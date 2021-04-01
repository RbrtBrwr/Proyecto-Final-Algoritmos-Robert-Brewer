# Jugador
from jugador import Player


# Juegos
from adivinanza import Adivinanza
from ahorcado import Ahorcado
from criptograma import Criptograma
from logicaB import LogicaB
from logicaE import LogicaE
from memoria import Memoria
from mezclada import PalabrasMezcladas
from numeroEntre import EscogeNumero
from pipes import Pipes
from pregunta_python import PreguntaPython
from quizz import Quizizz
from sopa import Sopita
from preg_mate import PregMate

class Object:
    def __init__(self, info, player):
        self.nombre = info['name']
        self.posicion = info['position']
        self.game_name = info['game']['name']
        self.player = player

        # Inicializo los juegos dependiendo del objeto
        if self.game_name == 'Adivinanzas':
            self.game = Adivinanza(info['game'], player)
        elif self.game_name == 'sopa_letras':
            self.game = Sopita(info['game'], player)
        elif self.game_name == 'Preguntas sobre python':
            self.game = PreguntaPython(info['game'], player)
        elif self.game_name == 'ahorcado':
            self.game = Ahorcado(info['game'], player)
        elif self.game_name == 'Preguntas matemáticas':
            self.game = PregMate(info['game'], player)
        elif self.game_name == 'Criptograma':
            self.game = Criptograma(info['game'], player)
        elif self.game_name == 'Encuentra la lógica y resuelve':
            self.game = LogicaE(info['game'], player)
        elif self.game_name == 'Quizizz Cultura Unimetana':
            self.game = Quizizz(info['game'], player)
        elif self.game_name == 'memoria con emojis':
            self.game = Memoria(info['game'], player)
        elif self.game_name == 'Lógica Booleana':
            self.game = LogicaB(info['game'], player)
        elif self.game_name == 'Juego Libre':
            self.game = Pipes(info['game'], player)
        elif self.game_name == 'Palabra mezclada':
            self.game = PalabrasMezcladas(info['game'], player)
        elif self.game_name == 'escoge un número entre':
            self.game = EscogeNumero(info['game'], player)
            
    # Activa el objeto para jugar el juego
    def activar(self):
        return self.game.play_game()

    # retorna el requisito para el juego
    def chequear(self, game):
        if type(game.requirement) == list:
            return game.requirement
        elif type(game.requirement) != str:
            return 0
        else:
            return game.requirement
    #  Muestra el mensaje csi el jugador no tiene lo requerido
    def mensaje_req(self, game):
        print(self.game.mensaje_req)


