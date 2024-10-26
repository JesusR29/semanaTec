"""Snake, classic arcade game.
Exercises
1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ['purple', 'green', 'blue', 'orange', 'gray' ]	

food_direction = vector(10, 0)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():

    global food_direction
    next_position = food + food_direction

    if not inside(next_position):
        food_direction.x = randrange(-10, 11, 20)
        food_direction.y = randrange(-10, 11, 20)

    food.move(food_direction)
    ontimer(move_food, 500)  # Llama a esta función cada 500 ms

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, 'green')
    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)


def set_colors():
    """Change colors of snake and food."""
    global snake_color
    global food_color
    
    snake_color = colors[randrange(len(colors))]
    food_color = colors[randrange(len(colors))]
    # Ensure food color is not the same as snake color
    while food_color == snake_color:
        food_color = colors[randrange(len(colors))]
    return snake_color, food_color

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
set_colors()
move()
move_food()
done()

