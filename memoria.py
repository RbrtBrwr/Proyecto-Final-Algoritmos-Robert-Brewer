from juego import Game
from random import randrange
from time import sleep
from jugador import Player

class Memoria(Game):
    def __init__(self, info, player):
        super().__init__(info, player)
        self.penalizacion = 0.25

    def mostrar_pista(self, y_coord, x_coord, grid):
        # Muestra emoji de la pareja escogida
        if self.player.pistas > 0:
            self.player.pistas -= 1
            search = grid[y_coord][x_coord][1]
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if i != y_coord or j != x_coord:
                        if grid[i][j][1] == search:
                            y_coord2 = i
                            x_coord2 = j
                            return y_coord2, x_coord2
        else:
            print('No tienes mas pistas')
            y_coord2, x_coord2 = 777, 777
            return y_coord2, x_coord2

    def reset_grid(self, old_grid, temp_grid):
        # Regresa el grid al que era antes de escoger
        for i in range(len(old_grid)):
            for key, value in old_grid[i].items():
                temp_grid[i][key] = value

        return temp_grid

    def grid_display(self, grid, grid_set):
        # Imprime el grid
        
        print('  | A  | B  | C  | D  |')
        print('  ~~~~~~~~~~~~~~~~~~~~~')
        for i in range(len(grid)):
            print(f'{i + 1} | ', end='')
            for j in range(len(grid[i])):
                if grid_set[i][j]:
                    print(grid[i][j][1], end=" | ")
                else:
                    print(grid[i][j][0], end=" | ")
            print()
            print('  ~~~~~~~~~~~~~~~~~~~~~')

    def clear_screen(self, wait=0):
        # Sube pantalla para que no se vea el grid pasado
        if wait == 1:
            sleep(2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    def select(self):
        # Selecciona coordenadas para escoger el emoji
        while True:
            x_coord = input('Ingrese letra de columna: ').lower()
            if x_coord == 'exit':
                y_coord = 444   
                x_coord = 444
                return y_coord, x_coord 
            elif x_coord == 'clue':
                return 100, 100

            elif x_coord == 'a':
                x_coord = 0
                break
            elif x_coord == 'b':
                x_coord = 1
                break
            elif x_coord == 'c':
                x_coord = 2
                break
            elif x_coord == 'd':
                x_coord = 3
                break
            else:
                print('Input invalido')

        while True:    
            y_coord = input('Ingrese numero de fila: ')
            if y_coord.lower() == 'exit':
                y_coord = 444   
                y_coord = 444
                return y_coord, y_coord 
            elif y_coord == 'clue':
                return 100, 100
            elif not y_coord.isnumeric():
                print('Input invalido')
                
            elif int(y_coord) not in range(1, 5):
                print('input invalido')
            else:
                y_coord = int(y_coord) - 1
                break


        return y_coord, x_coord

    def check_win(self, grid_set):
        # Chequea que se hayan encontrado todas las parejas
        for i in grid_set:
            for value in i.values():
                if not value:
                    return False
        
        return True
    
    def play_game(self):
        # LIsta para parejas encontradas
        done = []

        # Grid para inicializar
        grid = [[[' X','😀'],[' X','🙄'],[' X','🤮'],[' X','🥰']],
                [[' X','🤮'],[' X','😨'],[' X','🤓'],[' X','😷']],
                [[' X','😨'],[' X','🤓'],[' X','🥰'],[' X','😷']],
                [[' X','🤑'],[' X','🤑'],[' X','🙄'],[' X','😀']]]

        # Valores para los emojis al iniciar
        grid_set = [{0 : False, 1 : False, 2 : False, 3 : False}, 
                    {0 : False, 1 : False, 2 : False, 3 : False}, 
                    {0 : False, 1 : False, 2 : False, 3 : False}, 
                    {0 : False, 1 : False, 2 : False, 3 : False}]

        # Todos true para que el usuario vea los emojis al iniciar
        grid_show = [{0 : True, 1 : True, 2 : True, 3 : True}, 
                    {0 : True, 1 : True, 2 : True, 3 : True}, 
                    {0 : True, 1 : True, 2 : True, 3 : True}, 
                    {0 : True, 1 : True, 2 : True, 3 : True}]

        print('Memorizatelo y encuentra las parejas') 
        self.mostrar_reglas()           
        self.grid_display(grid, grid_show)
        self.clear_screen(1)

        while True:
            print('Ingresa las coordenadas de las parejas')
            if self.check_win(grid_set):
                self.grid_display(grid, grid_set)
                return self.ganador()

            self.grid_display(grid, grid_set)
            # Chequear que no sea uno de los emojis ya encontrados            
            checking = True
            while checking:
    
                y_coord, x_coord = self.select()
                if y_coord == 444 or x_coord == 444:
                    return False

                check = (y_coord, x_coord)

                if check in done:
                    print('Pareja encontrada')
                else:
                    checking = False

            temp_grid = self.reset_grid(grid_set, grid_show)
            temp_grid[y_coord][x_coord] = True
            guess_1 = grid[y_coord][x_coord][1]
            self.clear_screen()
            self.grid_display(grid, temp_grid)

            # Chequear que no sea uno de los emojis ya encontrados
            checking = True
            while checking:
                y_coord2, x_coord2 = self.select()
                check = (y_coord2, x_coord2)
                if check in done:
                    print('Pareja ya encontrada')
                else:
                    checking = False
            
            if y_coord2 == 100 or x_coord2 == 100:
                y_coord2, x_coord2 = self.mostrar_pista(y_coord, x_coord, grid)

            if y_coord2 != 777 and x_coord2 != 777:
                if guess_1 == grid[y_coord2][x_coord2][1]:
                    grid_set[y_coord][x_coord] = True
                    grid_set[y_coord2][x_coord2] = True
                    doneA = (y_coord, x_coord)
                    done.append(doneA)
                    doneB = (y_coord2, x_coord2)
                    done.append(doneB)
                else:
                    temp_grid[y_coord2][x_coord2] = True
                    self.grid_display(grid, temp_grid)
                    self.clear_screen(1)
                    temp_grid = self.reset_grid(grid_set, temp_grid)
                    self.penalizar

