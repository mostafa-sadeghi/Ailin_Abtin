import turtle
import random
import time


main_screen = turtle.Screen()
main_screen.bgcolor('black')
main_screen.setup(600, 600)
main_screen.title("Snake Game")
main_screen.tracer(False)


def create_turtle(t_shape, t_color):
    my_turtle = turtle.Turtle()
    my_turtle.shape(t_shape)
    my_turtle.color(t_color)
    my_turtle.penup()
    return my_turtle


snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")

def change_position():
    x = random.randint(-270, 270)
    y = random.randint(-270, 240)
    snake_food.goto(x, y)

change_position()

def close():
    global running
    running = False


root = main_screen._root
root.protocol("WM_DELETE_WINDOW", close)

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)

def go_up():
    snake_head.direction = "up"
def go_down():
    snake_head.direction = "down"
def go_right():
    snake_head.direction = "right"
def go_left():
    snake_head.direction = "left"


main_screen.listen()
main_screen.onkeypress(go_up, "Up")
main_screen.onkeypress(go_down, "Down")
main_screen.onkeypress(go_left, "Left")
main_screen.onkeypress(go_right, "Right")


running = True
while running:
    main_screen.update()
    if snake_head.distance(snake_food) < 20:
        change_position()

    move()
    time.sleep(0.2)
