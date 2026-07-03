import math

# Store calculation history
history = []


def add(a, b):
    result = a + b
    history.append(f"{a} + {b} = {result}")
    return result


def subtract(a, b):
    result = a - b
    history.append(f"{a} - {b} = {result}")
    return result


def multiply(a, b):
    result = a * b
    history.append(f"{a} * {b} = {result}")
    return result


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    result = a / b
    history.append(f"{a} / {b} = {result}")
    return result


def square_root(a):
    if a < 0:
        return "Square root of negative number not possible"

    result = math.sqrt(a)
    history.append(f"√{a} = {result}")
    return result


def show_history():
    if len(history) == 0:
        print("No history available")
    else:
        print("\nCalculation History:")
        for item in history:
            print(item)


while True:

    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Show History")
    print("7. Exit")

    choice = int(input("Enter your choice: "))


    if choice >= 1 and choice <= 4:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", add(num1, num2))

        elif choice == 2:
            print("Result =", subtract(num1, num2))

        elif choice == 3:
            print("Result =", multiply(num1, num2))

        elif choice == 4:
            print("Result =", divide(num1, num2))


    elif choice == 5:

        num = float(input("Enter number: "))
        print("Result =", square_root(num))


    elif choice == 6:

        show_history()


    elif choice == 7:

        print("Thank you for using calculator")
        break


    else:
        print("Invalid choice")
