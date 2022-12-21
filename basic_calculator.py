"""
Project: Basic Calculator
Author: Krystella Rattan
"""

# Steps:
# define the functions needed: add, subtract, multiply, divide

def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")  # "\n" creates a line break

def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer) + "\n")



# print options to the user
while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")



# ask for values

    choice = input("Input your choice: ")

# call the functions

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        add(a, b) # this calls the function
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Program ended")
        quit()

# while loop to continue the program until the user wants to exit
        # while True:
