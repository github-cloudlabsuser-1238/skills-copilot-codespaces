def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def percentage(x, y):
    return (x / y) * 100

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    """
    A simple calculator function that allows the user to perform basic arithmetic operations.
    
    The user can select from the following operations:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Percentage

    The function prompts the user to enter their choice of operation and two numbers to perform the operation on.
    It then performs the selected operation and prints the result.

    Note:
    - For addition, subtraction, multiplication, and division, the user must enter two numbers.
    - For percentage, the function calculates what percentage the first number is of the second number.
    - If an invalid choice is entered, the function prints "Invalid input".

    Returns:
        None
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"{num1} is {percentage(num1, num2)}% of {num2}")
        print("Invalid input")

if __name__ == "__main__":
    calculator()