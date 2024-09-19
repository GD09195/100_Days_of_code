from Day10_Calculator_Art import logo

def add(number1, number2):
    """Adds the two inputs """
    return number1+number2

def subtract(number1, number2):
    """Subtracts Number 2 from Number 1"""
    return number1-number2

def multiply(number1, number2):
    """Multiplies the two inputs""" 
    return number1 * number2

def divide(number1, number2):
    """Divides Number 1 by Number 2"""
    return number1 / number2

operations: dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)

def calculator():

    print(logo)

    num1 = float(input("First Number:"))

    for operator in operations:
        print(f"{operator}")

    str_operator = input("Choose your operation: ")
    num2 = float(input("Second Number:"))

    operator = operations[str_operator]

    answer = operator(num1, num2)
    print(f"{num1}{str_operator}{num2} = {answer}")

    while(True): 
        
        repetition = input(f"Type 'y' to continue calculation with {answer},\nType 'r' for new calculation \nType 'n' to exit:")
        if repetition == 'n':
            return
        elif repetition == 'r':
            calculator()
            return
        
        str_operator = input("Pick an operator: ")
        num4 = answer
        num3 = float(input("What's the next number: "))
        operator = operations[str_operator]
        answer = operator(num4, num3)

        print(f"{num4}{str_operator}{num3} = {answer}")

calculator()