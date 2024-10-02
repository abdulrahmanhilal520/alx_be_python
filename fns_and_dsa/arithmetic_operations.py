
def perform_operation(num1,num2,operation):
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")
    
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed")
                return None
        case _:
            print("Invalid operation. Please choose one of (+, -, *, /).")
            return None
    return result

num1 = 5
num2 = 3
operation = 'add'
result = perform_operation(num1, num2, operation)

if __name__ == "__main__":
    main()
