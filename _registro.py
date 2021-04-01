import json
from jugador import Player



def check_usuarios(nombre):
    """chequea si el nombre ingresado es un usuario registrado

    Args:
        nombre (str): username
    """
    f = open('_registro.json')
    registro = json.load(f)
    f.close()
    for i in registro:
        if i['username'] == nombre:
            return True
    return False

def check_password(nombre, contrasena):
    """chequea que la contrasena ingresada sea la correcta para el usuario

    """
    f = open('_registro.json')
    registro = json.load(f)
    f.close()
    for i in registro:
        if i['username'] == nombre:
            if i['password'] == contrasena:
                return True
            else:
                return False

def load_user(nombre):

    """carga usuario ya registrado

    """
    f = open('_registro.json')
    registro = json.load(f)
    f.close()
    for i in registro:
        if i['username'] == nombre:
            nombre = i['username']
            contrasena = i['password']
            edad = i['edad']
            avatar = i['avatar']
    
    return nombre, contrasena, edad, avatar

def register_new(jugador, tiempo):
    """registra usuario nuevo al ganar
    """

    if jugador.nuevo:
        datos = {}
        username = jugador.nombre
        avatar = jugador.avatar
        age, password = jugador.get_age_password()

        datos["username"] = username
        datos["password"] = password
        datos["edad"] = age
        datos["avatar"] = avatar
        datos["partidas"] = []
        

        partida = {}
    
        tiempo = tiempo
        vidas = jugador.vida
        pistas = jugador.pistas

        partida["tiempo"] = tiempo
        partida["vidas"] = vidas
        partida["pistas"] = pistas

        datos["partidas"].append(partida)
    
        # with open('registro.json', 'a') as outfile:
        #     json.dump(datos, outfile[0], indent=4)

        with open('_registro.json', 'r') as file:
            registro = json.load(file)


        registro.append(datos)

        with open('_registro.json', 'w') as outfile:
            json.dump(registro, outfile, indent=4)

    else:
        partida = {}
        tiempo = jugador.tiempo
        vidas = jugador.vida
        pistas = jugador.pistas

        partida["tiempo"] = tiempo
        partida["vidas"] = vidas
        partida["pistas"] = pistas

        f = open('_registro.json')
        registro = json.load(f)
        f.close()

        for i in registro:
            if i['username'] == jugador.nombre:
                i['partidas'].append(partida)

        with open('_registro.json', 'w') as outfile:
            json.dump(registro, outfile, indent=4)

def mejores_tiempos():
    """rankea a los jugadores por mejor tiempo realizado
    """
    top_times = []
    f = open('_registro.json')
    registro = json.load(f)
    f.close()

    while len(top_times) < 5:
        top_time = 1000
        top_name = ''
        for i in range(len(registro)):
            
            for x in range(len(registro[i]['partidas'])):
                if registro[i]['partidas'][x]['tiempo'] < top_time:
                    top_time = registro[i]['partidas'][x]['tiempo']
                    top_name = registro[i]['username']
                    indice_p = x
                    indice_i = i
        minutos = str(top_time // 60)
        segundos = str(top_time % 60)
        if len(segundos) == 1:
            segundos = '0'+segundos
        top_time = minutos + ':' + segundos
        top = (top_name, top_time)
        top_times.append(top)
        del registro[indice_i]['partidas'][indice_p]

    print('Los mejores jugadores, en orden de tiempo de juego:')
    for num, info in enumerate(top_times):
        print(f'{num + 1}. {info[0]}, {info[1]}')

def mas_jugadas():
    """rankea a los jugadores con mas jugadas
    """
    top_top = []
    f = open('_registro.json')
    registro = json.load(f)
    f.close()

    while len(top_top) < 3:
        top_veces = 1
        top_name = ''
        for i in range(len(registro)):
            if len(registro[i]['partidas']) >= top_veces:
                top_veces = len(registro[i]['partidas'])
                top_name = registro[i]['username']
                indice = i
        top = (top_name, top_veces)
        top_top.append(top)
        del registro[indice]

    print('Los Jugadores que mas han ganado')
    for num, info in enumerate(top_top):
        print(f'{num + 1}. {info[0]}, {info[1]} partidas')

# tester = Player('pedro', 12, 'chiguire', 'Un Sharpie', '10:00', 2, 11, ['azul', 'verde', 3], True)
# register_new(tester)