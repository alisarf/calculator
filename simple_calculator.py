''' Calculator'''
import time

print("Welcome to the Mighty Calculator\n")
time.sleep(1)
#Fxns: subtraction, addition, multiplication, division

def add():
    number_1 = int(input("Enter first number:"))
    number_2 = int(input("Enter second number:"))
    addition = number_1 + number_2
    time.sleep(1)
    print(number_1, "+", number_2, "=", addition )

def sub():
    number_1 = int(input("Enter first number:"))
    number_2 = int(input("Enter second number:"))
    subtraction = number_1 - number_2
    time.sleep(1)
    print(number_1, "-", number_2, "=", subtraction )

def mult():
    number_1 = int(input("Enter first number:"))
    number_2 = int(input("Enter second number:"))
    multiplication = number_1 * number_2
    time.sleep(1)
    print(number_1, "x", number_2, "=", multiplication )

def div():
    number_1 = int(input("Enter first number:"))
    number_2 = int(input("Enter second number:"))
    division = number_1 / number_2
    time.sleep(1)
    print(number_1, "/", number_2, "=", division )

#User instructions:
print("Please select an operation:\n" \
      "Addition: 'a'\n" \
      "Subtraction: 's'\n" \
      "Multiplication: 'm' \n" \
      "Division: 'd' \n" \
      "Quit at anytime with 'q'"
      )
time.sleep(1)

while True:
    time.sleep(1)
    operation = input("\nSelect an operation:")
    time.sleep(1)

    if operation == 'q':
        print("Terminating program")
        break
    elif operation == 'a':
        add()
    elif operation == 's':
        sub()
    elif operation == 'm':
        mult()
    elif operation == 'd':
        div()
    else:
        print("\nInvalid Input\nTry Again...")

