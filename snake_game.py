import turtle
main_screen = turtle.Screen()

def close():
    pass

root = main_screen._root
root.protocol("WM_WINDOW_DELETE", close)

running = True
while running:
    main_screen.update()
