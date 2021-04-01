import json



def get_avatars():
    """muestra los avatares del archivo 

    """
    
    f = open('_game_specs.json')

    specs = json.load(f)

    f.close()
    return specs['avatares']

def show_dificulty():
    """muestra las dificultades del archivo
    """
    
    f = open('_game_specs.json')

    specs = json.load(f)

    f.close()
    for key, value in specs['dificultades'].items():
        print(f'Dificultad: {key}')
        for i, j in value.items():
            if i == 'tiempo':
                print(f'{i}: {j} minutos')
            else:
                print(f'{i}: {j}')
        print()

def get_difficulty(setting):
    f = open('_game_specs.json')
    specs = json.load(f)
    f.close()

    for i in specs['dificultades']:
        if i == setting:
            vidas = specs['dificultades'][i]['vidas']
            tiempo = specs['dificultades'][i]['tiempo']
            pistas = specs['dificultades'][i]['pistas']
            return vidas, tiempo, pistas

    return vidas, tiempo, pistas
