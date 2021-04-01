from juego import Game
from random import randrange
from jugador import Player
from time import sleep

class Pipes(Game):
    def __init__(self, info, player):
        super().__init__(info, player)
        self.penalizacion = 1
        self.rules = 'Ingresa las coordenadas del tile que quiere girar, ganas cuando no queden lineas desconectadas'

        # Son los posibles arreglos de los pipes
        self.arreglos = {
                # podria poner esto en un diccionarios
                'simple' : {
                    'izquierda' : [[' ',' ',' ',' ', ' ',' ',' '], [' ','-','-','O',' ',' ',' '],[' ',' ',' ',' ', ' ',' ',' ']],
                    'derecha' : [[' ',' ',' ',' ', ' ',' ',' '], [' ',' ',' ','O','-','-',' '],[' ',' ',' ',' ', ' ',' ',' ']],
                    'arriba' : [[' ',' ',' ','|', ' ',' ',' '], [' ',' ',' ','O',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' ']],
                    'abajo' : [[' ',' ',' ',' ', ' ',' ',' '], [' ',' ',' ','O',' ',' ',' '], [' ',' ',' ','|',' ',' ',' ']],
                },

                's' : ['izquierda', 'arriba', 'derecha', 'abajo'],

                'doble' : {
                    'horizontal' : [[' ',' ',' ',' ', ' ',' ',' '], [' ','-','-','O','-','-',' '], [' ',' ',' ',' ',' ',' ',' ']],
                    'vertical' : [[' ',' ',' ','|', ' ',' ',' '], [' ',' ',' ','O',' ',' ',' '],[' ',' ',' ','|', ' ',' ',' ']]
                },
                'd' : ['horizontal','vertical'],

                'tubo' : {
                    'horizontal' : [[' ',' ',' ',' ', ' ',' ',' '], [' ','-','-','-','-','-',' '], [' ',' ',' ',' ',' ',' ',' ']],
                    'vertical' : [[' ',' ',' ','|', ' ',' ',' '], [' ',' ',' ','|',' ',' ',' '],[' ',' ',' ','|', ' ',' ',' ']]
                },
                'tu' : ['horizontal','vertical'],

                'te' : {
                    'izquierda' : [[' ',' ',' ','|', ' ',' ',' '], [' ','-','-','|',' ',' ',' '],[' ',' ',' ','|', ' ',' ',' ']],
                    'derecha' : [[' ',' ',' ','|', ' ',' ',' '], [' ',' ',' ','|','-','-',' '],[' ',' ',' ','|', ' ',' ',' ']],
                    'arriba' : [[' ',' ',' ','|', ' ',' ',' '], [' ','-','-','-','-','-',' '], [' ',' ',' ',' ',' ',' ',' ']],
                    'abajo' : [[' ',' ',' ',' ', ' ',' ',' '], [' ','-','-','-','-','-',' '], [' ',' ',' ','|',' ',' ',' ']]
                },
                't' : ['izquierda', 'arriba', 'derecha', 'abajo'],

                'codo' : { 
                'izquierda_abajo' : [[' ',' ',' ',' ',' ',' ',' '], [' ','-','-','¬',' ',' ',' '],[' ',' ',' ','|', ' ',' ',' ']],
                'izquierda_arriba' : [[' ',' ',' ','|', ' ',' ',' '], [' ','-','-','/',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' ']],
                'derecha_abajo' : [[' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ','/','-','-',' '],[' ',' ',' ','|', ' ',' ',' ']],
                'derecha_arriba' : [[' ',' ',' ','|', ' ',' ',' '], [' ',' ',' ','-','-','-',' '],[' ',' ',' ',' ',' ',' ',' ']]
                },
                "c" : ['izquierda_abajo','izquierda_arriba','derecha_arriba','derecha_abajo'],

                "space" : [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']],

                'separador_horizontal' : '  #################################'
                }
    def ganador(self):
        print('Ganaste!')
        self.availability = False
        sleep(2)
        return True

    def get_coords(self):
        # El jugador ingresa las coordenadas del tile que quiere mover
        while True:
            x = input('Ingrese la letra de la columna: ').lower()
            if x == 'clue':
                print('Como te seriviria una pista?')
            if x == 'a':
                x = 0
                break
            elif x == 'b':
                x = 1
                break
            elif x == 'c':
                x = 2
                break
            elif x == 'd':
                x = 3
                break
            elif x == 'exit':
                x, y = 404, 404
                return x, y
            
        while True:
            y = input('Ingrese el numero de la fila: ')
            if y == 'exit':
                x, y = 404, 404
                break
            elif y == 'clue':
                print('Para que quieres una pista?')
            elif not y.isnumeric():
                print('Opcion invalida')
                
            elif 1 > int(y) > 4:
                print('Ingresa un numero entre 1 y 4')
            else:
                y = int(y) - 1
                break

        return x, y

    def show_grid(self, set_grid):
        # Imprime el grid, se imprime fila por fila de los tiles en cada fila
        print('      A       B       C       D')
        num = 1
        for i in set_grid:  
            line1 = ['  #']
            line2 = [str(num), ' #']
            line3 = ['  #']
            num += 1
            for j in i:
                z = 0
                for x in j: 
                    z += 1
                    if z == 1:
                        for y in x:
                            line1.append(y)
                            
                    elif z == 2:
                        for y in x:
                            line2.append(y)
                            
                    elif z == 3:
                        for y in x:
                            line3.append(y)
                            
                line1.append('#')
                line2.append('#')
                line3.append('#')


            print(self.arreglos['separador_horizontal'])
            print(''.join(line1))
            print(''.join(line2))
            print(''.join(line3))
                        
        print(self.arreglos['separador_horizontal'])      

    def grid_play(self, posiciones):
        # Cambia la posicion de los tiless para hacerlos girar
        p00 = posiciones[0]
        p01 = posiciones[1]
        p02 = posiciones[2]
        p10 = posiciones[3]
        p11 = posiciones[4]
        p12 = posiciones[5]
        p13 = posiciones[6]
        p20 = posiciones[7]
        p21 = posiciones[8]
        p22 = posiciones[9]
        p23 = posiciones[10]
        p33 = posiciones[11]



        positions = [[self.arreglos['s'][p00], self.arreglos['tu'][p01],self.arreglos['c'][p02]], [self.arreglos['c'][p10], self.arreglos['d'][p11], self.arreglos['t'][p12], self.arreglos['c'][p13]], 
                    [self.arreglos['s'][p20], self.arreglos['s'][p21], self.arreglos['tu'][p22], self.arreglos['t'][p23]], [0,0,0, self.arreglos['t'][p33]]]

        set_grid = [[self.arreglos['simple'][positions[0][0]], self.arreglos['tubo'][positions[0][1]], self.arreglos['codo'][positions[0][2]], self.arreglos['space']],
                    [self.arreglos['codo'][positions[1][0]], self.arreglos['doble'][positions[1][1]], self.arreglos['te'][positions[1][2]], self.arreglos['codo'][positions[1][3]]], 
                    [self.arreglos['simple'][positions[2][0]], self.arreglos['simple'][positions[2][1]], self.arreglos['tubo'][positions[2][2]], self.arreglos['te'][positions[2][3]]],
                    [self.arreglos['space'], self.arreglos['space'], self.arreglos['space'], self.arreglos['simple'][positions[3][3]]]]

        


        
        self.show_grid(set_grid)   

        x, y = self.get_coords()        
        



        if y == 0:
            if x == 0:
                if p00 == 3:
                    p00 = 0
                else:
                    p00 += 1

            elif x == 1:
                if p01 == 0:
                    p01 = 1
                else:
                    p01 = 0

            elif x == 2:
                if p02 == 3:
                    p02 = 0
                else:
                    p02 += 1

            else:
                pass
                
        elif y == 1:
            if x == 0:
                if p10 == 3:
                    p10 = 0
                else:
                    p10 += 1
            
            elif x == 1:
                if p11 == 0:
                    p11 = 1
                else:
                    p11 = 0

            elif x == 2:
                if p12 == 3:
                    p12 = 0
                else:
                    p12 += 1


            elif x == 3:
                if p13 == 3:
                    p13 = 0
                else:
                    p13 += 1

        elif y == 2:
            if x == 0:
                if p20 == 3:
                    p20 = 0
                else:
                    p20 += 1
            
            elif x == 1:
                if p21 == 3:
                    p21 = 0
                else:
                    p21 += 1

            elif x == 2:
                if p22 == 0:
                    p22 = 1
                else:
                    p22 = 0

            elif x == 3:
                if p23 == 3:
                    p23 = 0
                else:
                    p23 += 1


        elif y == 3:
            if x == 3:
                if p33 == 3:
                    p33 = 0
                else:
                    p33 += 1

            else:
                pass

        check_values = [p00 , p01 , p02 , p10 , p11 , p12 , p13 , p20 , p21 , p22 , p23 , p33]
        return check_values

    def play_game(self):
        # Estas son las posiciones que se necesitan para ganar
        answers = [2, 0, 0, 3, 0, 1, 0, 1, 2, 0, 0, 1]

        # esto seria para brobar, creo que no lo uso
        answer_grid = [[self.arreglos['simple'][self.arreglos['s'][2]], self.arreglos['tubo'][self.arreglos['tu'][0]], self.arreglos['codo'][self.arreglos['c'][0]], self.arreglos['space']],
                    [self.arreglos['codo'][self.arreglos['c'][3]], self.arreglos['doble'][self.arreglos['d'][0]], self.arreglos['te'][self.arreglos['t'][1]], self.arreglos['codo'][self.arreglos['c'][0]]], 
                    [self.arreglos['simple'][self.arreglos['s'][1]], self.arreglos['simple'][self.arreglos['s'][2]], self.arreglos['tubo'][self.arreglos['tu'][0]], self.arreglos['te'][self.arreglos['t'][0]]],
                    [self.arreglos['space'], self.arreglos['space'], self.arreglos['space'], self.arreglos['simple'][self.arreglos['s'][1]]]]



        # Se mezclan las posiciones iniciales
        posiciones = [randrange(4), randrange(2), randrange(4), randrange(4), randrange(2), randrange(4), randrange(4), randrange(4), randrange(4), randrange(2), randrange(4), randrange(4)]
        self.mostrar_reglas()
        while True:

            
            posiciones = self.grid_play(posiciones)
            if posiciones == 404:
                return False
            elif posiciones == answers:
                self.show_grid(answer_grid)
                self.ganador()
                return True
