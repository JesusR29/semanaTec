from random import shuffle
from turtle import *

from freegames import path

car = path('car.gif')
# Cambiamos números por letras
tiles = list("ABCDEFGH") * 2
state = {'mark': None, 'taps': 0}
hide = [True] * 16

def square(x, y):
    """Dibuja un cuadro blanco con contorno negro en (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(100)
        left(90)
    end_fill()

def index(x, y):
    """Convierte coordenadas (x, y) en índice de tile."""
    return int((x + 200) // 100 + ((y + 200) // 100) * 4)

def xy(count):
    """Convierte el índice de tile en coordenadas (x, y)."""
    return (count % 4) * 100 - 200, (count // 4) * 100 - 200

def tap(x, y):
    """Actualiza el tap y los tiles ocultos."""
    spot = index(x, y)
    mark = state['mark']
    
    # Aumenta el contador de taps
    state['taps'] += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # Detectar cuando todos los cuadros estén destapados
    if all(not h for h in hide):
        print("¡Felicidades, has destapado todos los cuadros!")

def draw():
    """Dibuja la imagen y los tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Mostrar el número de taps
    up()
    goto(-170, 200)
    color('black')
    write(f"Taps: {state['taps']}", font=('Arial', 20, 'normal'))

    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 35, y + 30)  # Centramos las letras
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
