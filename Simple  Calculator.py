                   #Method 1
'''
import math

print("Welcome to the calculator")

num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))
choice =input("Choose operation (+,-,*,/): ")
if choice == '+':
    print("Result:", num1+num2)
elif choice == '-':
    print("Result:", num1-num2)
elif choice == "*":
    print("Result:", num1*num2)
elif choice == "/":
    if num2!=0:
        print("Result:", num1/num2)
    else:
        print("Error: Cannot be divided by zero")
else:
    print("Invalid operation")
'''

'''
                    #Method 2
import math
print('Welcome to calculator')

def num(a, b):
    choice = input("Enter operation (+,-,*,/): ")
    while True:
        if choice == '+':
            print("Result:", a+b)
        elif choice == '-':
            print("Result:", a-b)
        elif choice == "*":
            print("Result:", a*b)
        elif choice == "/":
            break
            if b!=0:
                print("Result:", a/b)
            else:
                print("Error: Cannot be divided by zero")
        else:
            print("Invalid operation")
        break
print(num(a = float(input('Enter number: ')),
    b = float(input("Enter number: "))))
'''

'''
                #Method 3
# Simple Calculator v2

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"


print("Welcome to Simple Calculator")

while True:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", add(num1, num2))

    elif operation == "-":
        print("Result:", subtract(num1, num2))

    elif operation == "*":
        print("Result:", multiply(num1, num2))

    elif operation == "/":
        print("Result:", divide(num1, num2))

    else:
        print("Invalid operation")

    cont = input("\nDo you want to continue? (yes/no): ").lower()
    if cont != "yes":
        print("Goodbye!")
        break
'''

# Simple Calculator v3 (Portfolio Version)

history = []

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Error: Cannot divide by zero"

def show_history():
    if not history:
        print("No calculations yet.")
    else:
        print("\n--- Calculation History ---")
        for item in history:
            print(item)

print("=== Smart Calculator ===")

while True:
    print("\nMenu:")
    print("1. New Calculation")
    print("2. View History")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        operation = input("Choose operation (+, -, *, /): ")

        if operation == "+":
            result = add(num1, num2)

        elif operation == "-":
            result = subtract(num1, num2)

        elif operation == "*":
            result = multiply(num1, num2)

        elif operation == "/":
            result = divide(num1, num2)

        else:
            print("Invalid operation")
            continue

        print("Result:", result)

        history.append(f"{num1} {operation} {num2} = {result}")

    elif choice == "2":
        show_history()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")