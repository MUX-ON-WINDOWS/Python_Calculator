from banner import banner
from cmath import pi

banner()

import cmath
import math
import const

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def pical(num1, num2):
    return num1 * num2

print(const.options)

select = int(input("Select your calculation option: \n"
                   "1, 2, 3, 4, 5, 6, 7: \n"))
# Add
if select == 1:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
# Subtract
elif select == 2:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
# Multiply
elif select == 3:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
#  Divide
elif select == 4:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
# Sqaure root
elif select == 5:
    number_1 = int(input("Enter your number: "))
    print("√", number_1, "=",
          math.sqrt(number_1))
# Raised to the power
elif select == 6:
    number_1 = int(input("Enter first number: "))
    number_2 = 2
    print(number_1, "^", number_2, "=",
                    math.pow(number_1, number_2))
# Calculated with PI
elif select == 7:
    number_1 = int(input("Enter your number: "))
    print(number_1, "*", "π", "=",
                    pical(number_1, cmath.pi))
else:
    print("Please select an valid number.")
