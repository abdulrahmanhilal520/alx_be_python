num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operations = str(input("choice the operation (+, -, *, /): "))

match operations:
        case '+':
                    total = num1 + num2
                            print(f"the value of operation equal to:{total} ")
                               
                                   case '-':
                                               total = num1 - num2
                                                       print(f"the value of operation equal to:{total} ")
                                                               
                                                                   case '*':
                                                                               total = num1 * num2
                                                                                       print(f"the value of operation equal to:{total} ")
                                                                                          
                                                                                             
