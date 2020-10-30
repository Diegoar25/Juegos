"""
Juego de Snake

Se modificó que cada vez que se abre el programa se cambia el color de la comida y de la serpiente.
Se modificó que la comida no saliera de la ventana.

"""


from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
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
	if numero_random == 0:
            square(body.x, body.y, 9, 'black')
            square(food.x, food.y, 9, 'green')
        if numero_random == 1:
            square(body.x, body.y, 9, 'cyan')
            square(food.x, food.y, 9, 'magenta')
        if numero_random == 2:
            square(body.x, body.y, 9, 'magenta')
            square(food.x, food.y, 9, 'blue')
        if numero_random == 3:
            square(body.x, body.y, 9, 'green')
            square(food.x, food.y, 9, 'black')
        if numero_random == 4:
            square(body.x, body.y, 9, 'blue')
            square(food.x, food.y, 9, 'pink')



    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
