def add (a, b):
    return a + b


def subtract (a, b):       
    return a - b            
def multiply (a, b):
    return a * b            
def divide (a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b    
def power (a, b):
    return a ** b           
def modulus (a, b):
    return a % b        
def floor_divide (a, b):        
    if b == 0:
        raise ValueError("Cannot perform floor division by zero.")
    return a // b
def average (numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    return sum(numbers) / len(numbers)
def maximum (numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    return max(numbers)
def minimum (numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    return min(numbers)             

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Divide")
    print("8. Average")
    print("9. Maximum")
    print("10. Minimum")
    print("11. Exit")

    choice = input("Enter choice (1-11): ")

    if choice == '11':
        print("Exiting the calculator.")
        break

    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == '6':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
        elif choice == '7':
            try:
                print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
            except ValueError as e:
                print(e)

    elif choice in ['8', '9', '10']:
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

        if choice == '8':
            try:
                print(f"Average = {average(numbers)}")
            except ValueError as e:
                print(e)
        elif choice == '9':
            try:
                print(f"Maximum = {maximum(numbers)}")
            except ValueError as e:
                print(e)
        elif choice == '10':
            try:
                print(f"Minimum = {minimum(numbers)}")
            except ValueError as e:
                print(e)
    else:
        print("Invalid input. Please enter a number between 1 and 11.") 


