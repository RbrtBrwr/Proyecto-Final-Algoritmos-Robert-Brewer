# Desktop/proyecto/ProyectoFinal/Cuartos
from sympy import Symbol, diff, sin, cos, tan, lambdify
from random import randrange
from math import pi
from fractions import Fraction
import re
game_mate = [
{
"question": "Calcula la derivada de la función evaluada en pi  f(x)=((sen(x))/2)",
"answer": "Validar con python si el resultado de la derivada es correcto",
"clue_1": "no hay pistas aquí jajajajaj"
},
{
"question": "Calcula la derivada de la función en pi/2  f(x)=((cos(x))/2 - (tan(x))/5)  ",
"answer": "Validar con python si el resultado de la derivada es correcto",
"clue_1": "no hay pistas aquí jajajajaj"
},
{
"question": "Calcula la derivada de la función en pi/3 f(x)=((sen(x))/5 -(tan(x)))",
"answer": "Validar con python si el resultado de la derivada es correcto",
"clue_1": "no hay pistas aquí jajajajaj"
}]


def opciones( ):
        opciones = game_mate
        opcion = randrange(len(opciones))
        respuestas = opciones[opcion]
        pregunta = respuestas['question']
        test = pregunta.split('=')
        test = test[1]


        return pregunta, test


# esto es lo que va en opciones
opciones = game_mate
opcion = randrange(len(opciones))
respuestas = opciones[opcion]
pregunta = respuestas['question']
test = pregunta.split('=')
test = test[1]
s = pregunta.split(' ')

try:
    evaluar = eval(s[8])
except:
    evaluar = eval(s[7])

print(pregunta)
formula = test.replace('sen', 'sin')
x = Symbol('x')
f = eval(formula)
f_prima = f.diff(x)

f_prima = lambdify(x, f_prima)
print(f_prima(evaluar))

num = f_prima(evaluar)
num = round(num, 2)
fraccion = Fraction(str(num))
print(num, fraccion)
# print(Fraction(f_prima(evaluar)))

answer = input('Ingresa la derivada evaluada en pi')



# clues = ['pista1', 'pista2', 'pista3']
# jugador_pistas = 5

# def mostrar_pista(clues, num):
#     try:
#         print(clues[num])
#         return True
#     except IndexError:
#         print('No hay mas pistas')
#         return False

# clue_num = 0
# while True:
#     respuesta = input('==> ')
#     if respuesta.lower() == 'exit':
#         break
#     elif respuesta.lower() == 'clue':
#         if jugador_pistas > 0:
#             if mostrar_pista(clues, clue_num):
#                 jugador_pistas -= 1
#                 clue_num += 1

# print(jugador_pistas)
# print(clue_num)


# check = '4'
# print(check.upper())

# from time import time, sleep

# start_clock = time()
# while True:
#     check_clock = time()
#     timer = check_clock - start_clock
#     seconds = int(timer % 60)
#     minutes = int(timer // 60)
#     print(minutes, seconds)
#     sleep(10)

# start_clock = time()
# start_time = 600

# while True:
#     check_clock = time()
#     timer = check_clock - start_clock
#     seconds = int(timer % 60)
#     tiempo_restante = start_time - seconds
#     minutes = int(tiempo_restante // 60)
#     seconds = int(tiempo_restante % 60)
#     print("{:02d}".format(minutes), ':', "{:02d}".format(seconds))
#     # print(minutes, seconds)
#     sleep(3)

# from _especificaciones import get_rewards

# # print(get_rewards())


# def timer(start_clock, start_time):
#     check_clock = time()
#     timer = check_clock - start_clock
#     print('timer: ', timer)
#     seconds = int(timer)
#     print('seconds: ', seconds)
#     tiempo_restante = start_time - seconds
#     minutes = int(tiempo_restante // 60)
#     seconds = int(tiempo_restante % 60)
#     print(minutes, seconds)

# start_clock = time()
# start_time = 12

# while True:
#     timer(start_clock, start_time)
#     sleep(10)


