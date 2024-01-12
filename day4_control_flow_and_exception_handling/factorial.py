# Given number
number = 5

# Check if the number is negative
if number < 0:
    factorial = "Factorial not defined for negative numbers"
else:
    factorial = 1
    while number > 0:
        factorial = factorial * number
        number = number - 1

# Result
print(factorial)

