from abc import ABC, abstractmethod
from random import choice, shuffle, randrange
from string import ascii_uppercase
from time import time, sleep
from jugador import Player


class Game(ABC):
    def __init__(self, info, player):
        self.name = info['name']
        self.requirement = info['requirement']
        self.award = info['award']
        self.rules = info['rules']
        self.questions = info['questions']
        self.availability = True
        self.player = player
        self.penalizacion = 0
        try:
            self.mensaje_req = info['message_requirement']
        except:
            self.mensaje_req = 'No req'


    def check_availability(self):
        # Chequea si el juego ya fue ganado
        if self.availability:
            check = self.requirement

            if self.jugador.check_inventory(check):
                return True
            else:
                return False
        else:
            return False

    def mostrar_reglas(self):
        # Muestra regas del juego
        print(self.rules)

    
    @abstractmethod
    def play_game(self):

        pass

    def penalizar(self):
        # Quita vida al jugador
        self.player.vida -= self.penalizacion
        if self.player.vida <= 0:
            self.player.vida = 0

    def ganador(self):
        # gana el juego y otorga reward
        print('Ganaste!')
        print(f'Recibes: {self.award}')
        self.availability = False
        sleep(2)
        return self.award

    def opciones(self):
        pass

    def mostrar_pista(self, clues, num):
        # Muestra pista si hay
        try:
            print(clues[num])
            return True
        except IndexError:
            print('No hay mas pistas')
            return False

