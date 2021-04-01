from objeto import Object
from jugador import Player
from _especificaciones import check_rooms

class Room:
    def __init__(self, name, player):
        self.nombre = name.strip()
        self.objetos = check_rooms(name)
        self.player = player

        # Inicializa los objetos por cuarto
        if self.nombre == "Laboratorio SL001":
            self.pizarra = Object(self.objetos[0], player)
            self.computadora_1 = Object(self.objetos[1], player)
            self.computadora_2 = Object(self.objetos[2], player)

        elif self.nombre == "Biblioteca":
            self.libros = Object(self.objetos[0], player)
            self.silla = Object(self.objetos[1], player)
            self.gabetas = Object(self.objetos[2], player)

        elif self.nombre == "Plaza Rectorado":
            self.saman = Object(self.objetos[0], player)
            self.banco_1 = Object(self.objetos[1], player)
            self.banco_2 = Object(self.objetos[2], player)

        elif self.nombre == "Pasillo Laboratorios":
            self.puerta = Object(self.objetos[0], player)

        elif self.nombre == "Cuarto de Servidores":
            self.puerta = Object(self.objetos[0], player)
            self.rack = Object(self.objetos[1], player)
            self.papelera = Object(self.objetos[2], player)

