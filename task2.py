def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        try:
            choice = int(input("Enter the operation number (1/2/3/4/5): "))

            if choice == 5:
                print("Exiting the calculator.")
                break

            if choice not in [1, 2, 3, 4]:
                print("Invalid input. Please select a valid operation.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)

            print("Result:", result)
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            print()

if __name__ == "__main__":
    calculator()
