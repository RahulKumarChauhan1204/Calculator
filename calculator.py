def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    while True:
        print("\n1. Calculate\n2. Exit")
        choice = input("Select an option: ")
        if choice == '2': break
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Enter operation (+, -, *, /): ")
            if op == '+': print(add(num1, num2))
            elif op == '-': print(subtract(num1, num2))
            elif op == '*': print(multiply(num1, num2))
            elif op == '/': print(divide(num1, num2))
        except ValueError:
            print("Invalid input: Please enter numeric values.")

if __name__ == "__main__":
    calculator()