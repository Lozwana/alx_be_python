num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ").strip()

match operation:
    case "+":
        sum = num1 + num2
        print(f"The result is {sum}.")
        
    case "-":
        subtraction = num1 - num2
        print(f"The result is {subtraction}.")
        
    case "*":
        multiplication = num1 * num2
        print(f"The result is {multiplication}.")
        
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            divide = num1 / num2
            print(f"The result is {divide}.")
        
    case _:
        print("Invalid oparator. Please use +, -, *, or /.")