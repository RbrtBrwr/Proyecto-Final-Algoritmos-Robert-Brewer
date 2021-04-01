import json
from random import choice
import requests

# Cuando haya internet
response = requests.get("https://api-escapamet.vercel.app/")
especificaciones = response.json()

# f = open('_especificaciones.json')
# especificaciones = json.load(f)
# f.close()


def get_rewards(): 
    """Saca los rewards de los juegos y los mete en una lista

    Returns:
        [list]: lista con los rewards
    """
    rewards = []
    for i in especificaciones:
        for x in i['objects']:
            if x['game']['award'] == 'título Universitario':
                rewards.append('Titulo Universitario')
            if x['game']['award'] != 'vida extra' and x['game']['award'] != 'Parar el cronómetro y ganar el juego':
                rewards.append(x['game']['award'])

    return rewards

def check_rooms(room_name):
    """Saca la informacion del cuarto pasado como arg

    Args:
        room_name ([str]): nombre del cuarto

    Returns:
        [dict]: diccionario con la info para ese cuarto
    """
    for i in range(len(especificaciones)):
        if especificaciones[i]['name'] == room_name:
            nombre_cuarto = especificaciones[i]['name']
            objetos = especificaciones[i]['objects']
    return objetos

