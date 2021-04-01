from jugador import Player
from cuarto import Room
from _especificaciones import *
from _registro import *
from _game_specs import *
from time import sleep, time
from xdibujitos import render_room



            
def dime_tu_edad():
    """registra edad del jugador

    Returns:
        int: edad del jugador
    """
    while True:
        edad = input('Ingresa tu edad\n==> ')
        if edad.isnumeric() and 12 < int(edad) < 115:
            return int(edad)
        elif edad.lower() == 'exit':
            return exit()
        else:
            print('Si tu edad no es un numero entre 12 y 115 no puedes jugar')

def avatar_select():
    """Selecciona un avatar para tu jugador

    Returns:
        str: nombre del avatar
    """
    avatares = get_avatars()
    while True:
        print('Escoge uno de los siguientes avatares:\n')
        for i, j in enumerate(avatares):
            print(f'{i + 1}. {j}')
        
        seleccion = input('==> ')
        if not seleccion.isnumeric():
            print('Opcion invalida')
            sleep(1)
        elif int(seleccion) in range(len(avatares) + 1):
            return avatares[int(seleccion) - 1]
        else:
            print('Opcion invalida')
            sleep(1)

def registrar():
    """Se registra un jugador nuevo o se ingresa, si el nombre dell jugador ya existe en la base de datos tiene la opcion de ingresar,
    si no, se registra un nuevo usuario

    Returns:
        str y booleano: si el usuario es nuevo, se toma nota para registrarlo como nuevo al final del juego si gana
    """
    while True:
        nombre = input('Ingrese nombre de usuario\n==> ')
        if nombre.lower() == 'exit':
            return exit()
        elif check_usuarios(nombre):
            check = input('Usuario ya registrado, desea ingresar otro nombre o ingresar con este usuario?\n1. Otro nombre\n2. Cargar usuario\n3. Salir\n==> ')
            if check == '1':
                continue
            elif check == '2':
                checking = True
                while checking:
                    contrasena = input(f'Ingrese la contrasena para el usuario {nombre}\n==> ')
                    if check_password(nombre, contrasena):
                        nuevo = False
                        nombre, contrasena, edad, avatar = load_user(nombre)
                        print(f'Bienvenido {nombre}!')
                        sleep(1)
                        return nombre, contrasena, edad, avatar, nuevo
                    else:
                        check = input('Contrasena invalida, si quiere volver a intentar ingrese 0\n==> ')
                        if check != '0':
                            checking = False
            elif check == '3':
                break
                
            else:
                print('Opcion invalida')
                sleep(1)
        else: 
            nuevo = True
            break
    print(f'Bienvenido {nombre}\n')
    while True:

        contrasena = input(f'Ingrese contrasena para el usuario {nombre}\n==> ')
        if len(contrasena) < 3:
            print('La contrasena debe tener minimo 3 caracteres')
        else:
            test = input('Vuelva a ingresar su contrasena\n==> ')
            if test == contrasena:

                edad = dime_tu_edad()
                avatar = avatar_select()

                return nombre, contrasena, edad, avatar, nuevo
            else:
                print('Las contrasenas que ingreso no son iguales')

def game_difficulty():
    """Escoje la dificultad del juego

    Returns:
        int: numero de vidas, pistas y minutos que tendra el jugador
    """
    while True:
        show_dificulty()
        dif = input('Ingrese la dificultad que desea: ').lower()
        if dif == '1' or dif == 'facil':
            dif = 'facil'
            break
        elif dif == '2' or dif == 'media':
            dif = 'media'
            break
        elif dif == '3' or dif == 'dificil':
            dif = 'dificil'
            break
        else:
            print('Opcion invalida')
            
    vidas, tiempo, pistas = get_difficulty(dif)
    if vidas != 0:
        if tiempo < 5:
            tiempo = 5
        if vidas < 0:
            vidas = 1

        input(f'Has elegido la dificultad {dif}, tendras:\n{vidas} vidas\n{tiempo} minutos\n{pistas} pistas\n\nPresiona cualquier tecla para continuar')
        if vidas == 1:
            print('tip: no pises el saman')
            
        return vidas, tiempo, pistas
        
    else:
        print('Dificultad invalida\n')
        sleep(1)

def game_over(razon, player, minutes=0, seconds=0, tiempo_inicial=0):
    """Termina el juego, s el jugador gano se registra en la base de datos, si no, no
    muestra una pantalla final dependiendo de la razon por la que se haya terminado el juego

    Args:
        razon (str): razon para terminar el juego
        player (Player): jugador
        minutes (int, optional): minutos restantes. Defaults to 0.
        seconds (int, optional): segundos restantes en el minuto. Defaults to 0.
        tiempo_inicial (int, opcional): segundos con los que empezo el jugador

    Returns:
        exit(): sale del programa al terminar el juego
    """
    tiempo_total = (minutes * 60) + seconds
    if tiempo_total > 0:
        minutes = (tiempo_inicial - tiempo_total) // 60
        seconds = (tiempo_inicial - tiempo_total) % 60

    print(minutes, seconds)

    if razon == 'muerte':
        cambio_de_cuartos(1, player, minutes, seconds, 111)
        sleep(5)
        return exit()
    
    elif razon == 'tiempo':
        cambio_de_cuartos(1, player, minutes, seconds, 101)
        sleep(5)
        return exit()
    
    elif razon == 'ganador':
        cambio_de_cuartos(1, player, minutes, seconds, 100)
        sleep(5)
        register_new(player, tiempo_total)
        print(f'Has salvado la universidad!\nel nombre {player.nombre} sera registrado y conocido hasta el fin de la historia!'.upper())
        print('o hasta que se borre el json')
        input('Presiona cualquier tecla para salir')
        return exit()

def timer(start_clock, start_time):
    """[summary]

    Args:
        start_clock (int): tiempo al que se inicia el juego
        start_time (int): tiempo que tiene el jugador en segundos

    Returns:
        [int]: minutos y segundos del minuto restantes en el juego
    """
    check_clock = time()
    seconds = int(check_clock - start_clock)
    tiempo_restante = start_time - seconds
    minutes = int(tiempo_restante // 60)
    seconds = int(tiempo_restante % 60)
    return minutes, seconds
    
def iniciar():
    """inicializa el jugador con los datos introducidos o cargados

    Returns:
        [Player]: el objeto jugador
    """
    nombre, contrasena, edad, avatar, nuevo = registrar()
    
    
    vidas, tiempo, pistas = game_difficulty()
    inventario = get_rewards()
    player_1 = Player(nombre, edad, contrasena, avatar, tiempo, vidas, pistas, inventario, nuevo)
    return player_1

def init_rooms(player):
    """Inicializa los objetos Rooms para el juego

    Args:
        player (Player): es el jugador, este esta vinculado a todos los demas objetos

    Returns:
        Room: retorna los objetos rooms para le juego
    """
    laboratorio = Room('Laboratorio SL001', player)
    biblioteca = Room('Biblioteca', player)
    plaza = Room('Plaza Rectorado', player)
    pasillo = Room('Pasillo Laboratorios ', player)
    servidores = Room('Cuarto de Servidores ', player)
    return laboratorio, biblioteca, plaza, pasillo, servidores

def cambio_de_cuartos(vida, player, minutes, seconds, num_cuarto=1):
    """Elije el cuarto a mostrar y lo renderiza

    Args:
        vida (int): vida con la que inicia el jugador
        player (Player): jugador
        minutes (int): minutos restantes
        seconds (int): segundos restantes en el minuto
        num_cuarto (int, optional): los cuartos se elijen a traves de su numero, sumar o restar cambia el cuarto. Defaults to 1.
    """
    if num_cuarto == 0:
        cuarto = 'Plaza Rectorado'
    elif num_cuarto == 1:
        cuarto = 'Biblioteca'
    elif num_cuarto == 2:
        cuarto = 'Pasillo Laboratorios'
    elif num_cuarto == 3:
        cuarto = 'Laboratorios SL001'
    elif num_cuarto == 4:
        cuarto = 'Cuarto de Servidores'
    elif num_cuarto == 100:
        cuarto = 'ganador'
    elif num_cuarto == 101:
        cuarto = 'tiempo'
    elif num_cuarto == 111:
        cuarto = 'muerto'
        
        
    render_room(vida, cuarto, player, minutes, seconds)

def main():
    # Inputs para mover de cuarto
    movimientos = {'izquierda':['<', 'izquierda','left', 'i','l'], 'derecha':['>','derecha','right','d','r']}

    begin = input('BIENVENIDO\nPRESIONE ENTER\n\n==> ')
    if begin.lower() == 'estadisticas':
        mejores_tiempos()

        print('\n\n')
        mas_jugadas()

    else:

        player_1 = iniciar()
        # Tiempo con el que inicia el jugador (segundos)
        tiempo_inicial = player_1.tiempo * 60
        # contrasena para computadora 2
        contrasena = player_1.inventario.contrasena
        # Vida con la que inicia el jugador
        vida = player_1.vida
        # cuartos inicializados
        laboratorio, biblioteca, plaza, pasillo, servidores = init_rooms(player_1)

        # Narrativa 1
        print(f'''Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no
es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del
cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y asignaturas.
Necesitamos que nos ayudes a recuperar el disco, para eso tienes
{player_1.tiempo} minutos, antes de que el servidor se caiga y no se pueda hacer
más nada. ¿Aceptas el reto?\n''')
        algo = input('Presiona cualquier tecla para acepar y continuar. Si deseas salir ingresa "EXIT"\n==> ').lower()
        if algo == 'exit':
            exit()

        # Narrativa 2
        print(f'''Bienvenid@ {player_1.nombre}, gracias por tu disposición a ayudarnos a
resolver este inconveniente, te encuentras actualmente ubicad@ en la biblioteca, revisa el
menú de ayuda para ver qué acciones puedes realizar. Recuerda que el tiempo corre
más rápido que un trimestre en este reto.\n''')
        input('Presiona cualquier tecla para continuar\n==>')

        # Instrucciones
        render_room(vida, 'inicio', player_1, 0, 0)
        check = input('Presione cualquier tecla para comenzar el juego\n==> ')

        # Empieza a correr eltiempo
        start_clock = time()
        start_time = player_1.tiempo * 60
        num_cuarto = 1
        while True:
            # Si el jugador se queda sin vidas pierde
            if player_1.vida <= 0:
                game_over('muerte', player_1)

            # Cada vez que el jugador interactua con el juego principal (fuera de un minijuego), se le muestra su tiempo, este siempre esta corriendo
            minutes, seconds = timer(start_clock, start_time)
            
            # Si el jugador se queda sin tiempo pierde
            if minutes < 0:
                game_over('tiempo', player_1)

            # Cada vez que itera el while loop muestra el cuarto en el que esta el jugador
            cambio_de_cuartos(vida, player_1, minutes, seconds, num_cuarto)

            # User input
            ui = input('==> ').lower()

            # Cambia de cuarto al de la izquierda
            if ui in movimientos['izquierda']:
                if num_cuarto == 0:
                    num_cuarto = 1
                elif num_cuarto <= 4:
                    num_cuarto -= 1
                else:
                    print('No puedes ir hacia alla')

            # Cambia de cuarto a la derecha
            elif ui in movimientos['derecha']:
                if num_cuarto == 2 and not player_1.check_inventory('libro de Física'):
                    print('La puerta esta cerrada')
                    sleep(1)
                elif num_cuarto == 4:
                    print('No puedes ir hacia alla')
                    sleep(1)
                else:
                    num_cuarto += 1

            # Muestra la pantalla de ayuda
            elif ui == 'ayuda':
                render_room(vida, 'inicio', player_1, 0, 0)
                input('Presiona cualquier boton para continuar')

            # Muestra el inventario
            elif ui == 'inventario':
                player_1.ver_inventario()
                input('Presiona cualquier tecla para continuar\n==> ')

            # Salir del juego
            elif ui == 'exit':
                check = input('Si sale del juego perdera todo su progreso. \nSi desea salir ingrese "CONFIRMAR"\n==> ').lower()
                if check == 'confirmar':
                    break
            # Acciones para los cuartos, primero chequea si el juego ya fue ganado, luego si el objeto a activar tiene un requerimiento 
            #   Chequea que el jugador lo tenga en el inventario y si lo tiene juega, si no hay requerimiento juega 

            # Acciones para plaza
            elif num_cuarto == 0:
                if ui == 'banco 1':
                    game = plaza.banco_1.game
                    
                    if game.availability:
                        prize = plaza.banco_1.activar()
                        player_1.add_inventory(prize)
                    else:
                        print('Ya ganaste aqui')
                        sleep(1)

                elif ui == 'banco 2':
                    game = plaza.banco_2.game
                    if game.availability:
                        prize = plaza.banco_2.activar()
                        player_1.add_inventory(prize)
                    else:
                        print('Ya ganaste aqui')
                        sleep(1)

                elif ui == 'saman':
                    game = plaza.saman.game
                    requirement = plaza.saman.chequear(game)
                    requirement_1, requirement_2 = requirement[0], requirement[1]
                    if not game.availability:
                        print('Ya ganaste aqui')
                        sleep(1)
                        

                    elif player_1.check_inventory('título Universitario') and player_1.check_inventory('Mensaje'):
                        prize = plaza.saman.activar()
                        player_1.add_inventory(prize)

                    else:
                        plaza.saman.mensaje_req(game)
                        sleep(1)
                        plaza.saman.game.penalizar()

                else:
                    print('Opcion invalida')
                    sleep(1)
            
            # Acciones para biblioteca
            elif num_cuarto == 1:
                if ui == 'mueble de libros':
                    game = biblioteca.libros.game
                    if game.availability:
                        prize = biblioteca.libros.activar()
                        player_1.add_inventory(prize)
                    else:
                        print('Ya ganaste aqui')
                        sleep(1)

                elif ui == 'mueble de sentarse':

                    game = biblioteca.silla.game
                    requirement = biblioteca.silla.chequear(game)
                    if not game.availability:
                        print('Ya ganaste aqui')
                        sleep(1)
                    elif player_1.check_inventory(requirement):
                        prize = biblioteca.silla.activar()
                        player_1.add_inventory(prize)
                    else:
                        biblioteca.silla.mensaje_req(game)
                        sleep(1)

                elif ui == 'mueble de gabetas':
                    game = biblioteca.gabetas.game
                    requirement = biblioteca.gabetas.chequear(game)
                    if not game.availability:
                        print('Ya ganaste aqui')
                        sleep(1)
                    elif player_1.check_inventory(requirement):
                        prize = biblioteca.gabetas.activar()
                        player_1.add_inventory(prize)
                    else:
                        biblioteca.gabetas.mensaje_req(game)
                        sleep(1)

                else:
                    print('Opcion invalida')
                    sleep(1)

            # Acciones para pasillo labs
            elif num_cuarto == 2:
                if ui == 'puerta':
                    game = pasillo.puerta.game
                    requirement = pasillo.puerta.chequear(game)
                    if not game.availability:
                        print('Ya ganaste aqui')
                        sleep(1)

                    elif player_1.check_inventory(requirement):
                        prize = pasillo.puerta.activar()
                        player_1.add_inventory(prize)

                    else:
                        pasillo.puerta.mensaje_req(game)
                        sleep(1)

                else:
                    print('Opcion invalida')
                    sleep(1)

            # Acciones para laboratorio
            elif num_cuarto == 3:
                if ui == 'computadora 1':
                    game = laboratorio.computadora_1.game
                    requirement = laboratorio.computadora_1.chequear(game)

                    if not game.availability:
                        print('Ya ganaste aqui')
                        sleep(1)

                    elif player_1.check_inventory(requirement):
                        prize = laboratorio.computadora_1.activar()
                        player_1.add_inventory(prize)

                    else:
                        laboratorio.computadora_1.mensaje_req(game)
                        sleep(1)
                
                elif ui == 'computadora 2':
                    game = laboratorio.computadora_2.game
                    requirement = laboratorio.computadora_2.chequear(game)
                    
                    if not game.availability:
                        print('Ya ganaste aqui')
                        sleep(1)

                    else:
                        psswrd = input('Introducir Contrasena: ')
                        if not psswrd.isnumeric():
                            print('Contrasena Incorrecta')
                            sleep(1)

                        elif psswrd == contrasena:
                            prize = laboratorio.computadora_2.activar()
                            player_1.add_inventory(prize)

                        else:
                            print('Contrasena Incorrecta')
                            sleep(1)


                elif ui == 'pizarra':
                    game = laboratorio.pizarra.game
                    if game.availability:
                        prize = laboratorio.pizarra.activar()
                        player_1.add_inventory(prize)

                    else:
                        print('Ya ganaste aqui')
                        sleep(1)
                else:
                    print('Opcion invalida')
                    sleep(1)

            # Acciones para cuarto de servidores
            elif num_cuarto == 4:
                if ui == 'papelera':
                    game = servidores.papelera.game
                    if game.availability:
                        prize = servidores.papelera.activar()
                        player_1.add_inventory(prize)

                    else:
                        print('Ya ganaste aqui')
                        sleep(1)

                elif ui == 'puerta':
                    game = servidores.puerta.game
                    requirement = servidores.puerta.chequear(game) 
                    if not game.availability:
                        print('Ya ganaste aqui')
                        sleep(1)    

                    elif player_1.check_inventory(requirement):
                        if servidores.puerta.activar():
                            # Aqui se gana el juego
                            game_over('ganador', player_1, minutes, seconds, tiempo_inicial)

                    else:
                        servidores.puerta.mensaje_req(game)
                        sleep(1)


                elif ui == 'rack':
                    game = servidores.rack.game
                    if game.availability:
                        prize = servidores.rack.activar()
                        player_1.add_inventory(prize)
                    else:
                        print('Ya ganaste aqui')
                        sleep(1)
                else:
                    print('Opcion invalida')
                    sleep(1)

    
main()


