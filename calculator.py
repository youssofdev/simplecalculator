import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Function to calculate the square root of a number
def square_root(x):
    if x < 0:
        return "Invalid input (negative number)"
    return math.sqrt(x)

# Function to calculate the exponentiation of a number
def exponentiate(x, y):
    return x ** y

# Main function to take user input and perform calculations
def calculator():
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'square' for square root")
        print("Enter 'power' for exponentiation")
        print("Enter 'clear' to clear the screen")
        print("Enter 'quit' to end the program")
        
        user_input = input(": ")
        
        if user_input == "quit":
            break
        elif user_input in ("add", "subtract", "multiply", "divide", "square", "power"):
            if user_input == "square" or user_input == "power":
                num1 = float(input("Enter a number: "))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            
            if user_input == "add":
                print("Result: ", add(num1, num2))
            elif user_input == "subtract":
                print("Result: ", subtract(num1, num2))
            elif user_input == "multiply":
                print("Result: ", multiply(num1, num2))
            elif user_input == "divide":
                print("Result: ", divide(num1, num2))
            elif user_input == "square":
                print("Result: ", square_root(num1))
            elif user_input == "power":
                exponent = float(input("Enter the exponent: "))
                print("Result: ", exponentiate(num1, exponent))
        elif user_input == "clear":
            # Clear the screen for better user experience (works on most terminals)
            print("\033c")
        else:
            print("Invalid input. Please enter a valid option.")

# Call the calculator function to start the program
calculator()
