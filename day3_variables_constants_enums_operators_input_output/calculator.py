num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operator = input("Enter the operator (+, -, *, /): ")

if num1.isnumeric() and num2.isnumeric():
    num1 = float(num1)
    num2 = float(num2)

    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)
else:
    print("Invalid input! Please enter valid numeric values.")
