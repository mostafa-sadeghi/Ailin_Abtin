number1 = float(input("enter a number: "))
number2 = float(input("enter a number: "))

operator = input("(+  -   *   /): ")

if operator == "+":
    print(f'{number1} + {number2} = {number1 + number2}')
elif operator == "-":
    print(f'{number1} - {number2} = {number1 - number2}')
elif operator == "*":
    print(f'{number1} * {number2} = {number1 * number2}')
elif operator == "/":
    print(f'{number1} / {number2} = {number1 / number2}')