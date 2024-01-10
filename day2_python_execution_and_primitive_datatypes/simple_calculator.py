"""
Simple Calculator:
- Write a Python program that performs basic arithmetic operations (addition, subtraction, multiplication, division) on two user-input numbers.
- Handle different data types gracefully and provide appropriate output messages.
"""

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if num1.isnumeric() and num2.isnumeric():
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
else:
    print("Invalid input! Please enter valid numeric values.")