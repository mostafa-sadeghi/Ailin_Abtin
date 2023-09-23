# for i in range(50):
#     print("loop")


# i = 0
# while i < 50:
#     print("loop")
#     i += 1

# while True:
#     user_choice = input("Do you want to continue (y or n)? ")
#     if user_choice == "y":
#         continue
#     elif user_choice == "n":
#         break


# number = [1,2,3,4,5,6,7,8,9]
# total = 0
# for i in range(len(number)):
#     total += number[i]
# print(f"total is : {total}")

# total = 0
# i = 0
# while i < len(number):
#     total += number[i]
#     i += 1

# print(f"total is : {total}")


# def my_print(anything):
#     sent = "* " + anything + " *"
#     print(sent)


# my_print("hello")
# my_print("hello everybody")


# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False


# if is_even(13):
#     print("the number is even")
# else:
#     print("the number is odd")


# def area(length, width):
#     return f"The area is :{length * width}"


# def perimeter(length, width):
#     return f"The perimeter is : {2 * (length + width)}"


# length = float(input("enter the length: "))
# width = float(input("enter the width: "))
# print(area(length, width))
# print(perimeter(length, width))


import turtle

main_screen = turtle.Screen()
main_screen.bgcolor("orange")
main_screen.setup(600,600)
main_screen.title("my app")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(2)
my_turtle.pensize(3)
my_turtle.color("red")

sides = int(main_screen.textinput("sides", "How many sides? "))
for i in range(sides):
    my_turtle.forward(120)
    my_turtle.left(360/sides)

# TODO do it with while loop

turtle.done()