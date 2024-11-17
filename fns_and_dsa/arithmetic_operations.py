def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower().lower()

    if operation == "add":
        result = num1 + num2
        print(f"{num1},{num2}, {operation}")
    elif operation == "subtract":
        result = num1 - num2
        print(f"{num1},{num2}, {operation}")
    elif operation == "multiply":
        result = num1 * num2
        print(f"{num1},{num2}, {operation}")
    elif operation == "divide":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
        print(f"{num1},{num2}, {operation}")
    else:
        print("Invalid operation.")
        return

   

perform_operation()
