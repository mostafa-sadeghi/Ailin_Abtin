import turtle
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
snake_food = create_turtle("circle", "red")
snake_food.goto(100, 100)

# TODO به جای اینکه در شروع بازی غذای مار در مکان ثابت قرار داشته باشد، مکان غذای مار تصادفی باشد


def close():
    global running
    running = False


root = main_screen._root
root.protocol("WM_DELETE_WINDOW", close)

running = True
while running:
    main_screen.update()
