num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = str(input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        total = num1 + num2
        print(f"The value of the operation is: {total}")
    case '-':
        total = num1 - num2
        print(f"The value of the operation is: {total}")
    case '*':
        total = num1 * num2
        print(f"The value of the operation is: {total}")
    case '/':
        if num2 != 0:
            total = num1 / num2
            print(f"The value of the operation is: {total}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please choose one of (+, -, *, /).")
