def welcome_msg():
    print(
        f"\t\t☆*: .｡. o(≧▽≦)o .｡.:*☆ Welcome To ARITHMETIC OPERATIONAL CALCULATOR ☆*: .｡. o(≧▽≦)o .｡.:*☆ ")
    print("→ Press 1 to SUM of two numbers: \n→ Press 2 to SUBTRACT of two numbers: \n→ Press 3 to MULTIPLICATION two numbers:  \n→ Press 4 to DIVISION two numbers:  \n→ Press 5 to SQUARE of a number: \n→ Press 6 to SQUARE ROOT of a number: \n→ Press 7 to exit(): \n")


def sum(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def product(num1, num2):
    return num1 * num2


def square(num1):
    return num1 ** 2


def squareroot(num1):
    return num1 ** 0.5


def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ZeroDivisionError("Division by zero is not allowed")


def get_input():
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    return num1, num2


welcome_msg()
while True:
    choice = int(input("Enter Your Choice: \n"))
    if choice == 1:
        num1, num2 = get_input()
        result = sum(num1, num2)
        print(f"Result of Sum of Two Numbers is: {result}")

    elif choice == 2:
        num1, num2 = get_input()
        result = subtract(num1, num2)
        print(f"Result of Subtraction of Two Numbers is: {result}")

    elif choice == 3:
        num1, num2 = get_input()
        result = product(num1, num2)
        print(f"Result of Multiplication of Two Numbers is: {result}")

    elif choice == 4:
        num1, num2 = get_input()
        try:
            result = division(num1, num2)
            print(f"Result of Division of Two Numbers is: {result}")

        except ZeroDivisionError as e:
            print(e)
    elif choice == 5:

        num1 = int(input("Enter Number: "))
        result = square(num1)
        print(f"Result of Square of a Number is: {result}")

    elif choice == 6:
        num1 = int(input("Enter Number: "))
        result = squareroot(num1)
        print(f"Result of Square Root of a Number is: {result}")

    elif choice == 7:
        exit(0)
    else:
        print("Invalid Choice")
