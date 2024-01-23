# Lambda Functions (Anonymous Functions)
- **Lambda functions**, also known as **anonymous functions**, are a feature of many programming languages, including Python. 
- They are called "anonymous" because they do not need to be named. 
- They are most useful for short functions that are used only once, or for a short period of time. 

## Understanding Lambda Functions
- In Python, lambda functions are defined using the lambda keyword, followed by a list of parameters, a colon, and the expression to evaluate and return.
- Syntax: `lambda arguments: expression`

#### Example 1: A simple lambda function
This lambda function takes one parameter (x) and returns its square (x * x).
```python
# Define a lambda function
square = lambda x: x * x

# Use the lambda function
print(square(5))  # Output: 25
```

#### Example 2: Lambda with multiple arguments
This lambda function takes two parameters (x and y) and returns their product (x * y).
```python
# Define a lambda function
multiply = lambda x, y: x * y

# Use the lambda function
print(multiply(2, 3))  # Output: 6
```

## When to Use Lambda Functions
- Lambda functions are best used in scenarios where you need a simple function for a short period of time, and you prefer not to formally define a function using def. 

Common use cases include:
#### 1. map Function:
- The `map` function applies a given function to each item of an iterable (like a list) and returns a map object (which is an iterator). 
- When used with a lambda function, you can apply a quick operation to each element in the list without formally defining a function.

```python
# WITHOUT LAMBDA
def square(number):
    return number ** 2

numbers = [1, 2, 3, 4]
squared = list(map(square, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```
```python
# WITH LAMBDA
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```
#### 2. filter Function:
- The `filter` function constructs an iterator from elements of an iterable for which a function returns true. 
- In combination with a lambda function, filter can be used to filter items out of a sequence.
```python
# WITHOUT LAMBDA
def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]

```
```python
# WITH LAMBDA
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```
#### 3. reduce Function:
- The `reduce` function, which is part of the functools module, applies a function of two arguments cumulatively to the items of a sequence, from left to right, so as to reduce the sequence to a single value. 
- This is useful for performing some computation on a list and, unlike map and filter, returns a single value as a result.
```python
# WITH LAMBDA
from functools import reduce

def sum_numbers(x, y):
    return x + y

numbers = [1, 2, 3, 4]
summed = reduce(sum_numbers, numbers)
print(summed)  # Output: 10
```
```python
from functools import reduce
numbers = [1, 2, 3, 4]
summed = reduce(lambda x, y: x + y, numbers)
print(summed)  # Output: 10
```

## When Not to Use Lambda Functions
#### 1. When the function is complex: 
- If your function is beyond a simple expression, it's better to define it using def for the sake of clarity.
```python
# Don't do this
complex_function = lambda x: (some complex set of operations)

# Do this
def complex_function(x):
    # some complex set of operations
    return result
```
#### 2. When the function will be used multiple times: 
- If a function is going to be used in several places in your code, it's better to define it once using def and refer to it by name.
#### 3. When you need proper documentation: 
- Lambda functions are limited in that they cannot have their own documentation via docstrings. 
- If you need to document the behavior of the function, it's better to use `def`.
#### 4. When you want to use multiple expressions or statements: 
- Lambda functions are limited to a single expression. 
- If you need multiple expressions or statements (e.g., loops, multiple statements), you should define a regular function using `def`.

---
# Recursion
- Recursion is a powerful programming paradigm where a function calls itself to solve a problem. 
- This technique allows complex problems to be broken down into simpler ones, following the divide-and-conquer strategy. 
- It's particularly useful in scenarios where the solution involves repeating a similar operation at each step, but with a smaller or simpler input. 
- Recursion continues until it reaches a **base case**, a condition that ends the recursive calls, preventing an infinite loop. 
- While recursion can offer elegant and concise solutions, it's essential to handle it with care due to potential issues like stack overflow or excessive memory usage.

### Understanding Function Frames in Recursion
- In programming, recursion is facilitated by the use of **function frame**s or **stack frames**. 
- Each time a recursive function is called, a new frame is created and placed on top of the call stack. 
- This frame holds the function's local variables, parameters, and the return address. 
- When a function reaches its base case, it returns, and its frame is removed (or popped) from the stack, handing control back to the frame of the previous recursive call.

Practical Examples of Recursion

### 1. Print Numbers from m to n
Printing numbers from m to n showcases how recursion can simplify operations that would otherwise require iterative loops.
#### Without Recursion (Iterative Approach)
```python
def print_numbers_iteratively(m, n):
    for i in range(m, n + 1):
        print(i)
```
#### With Recursion
The recursive version calls itself with an incremented value of m, printing each number until m exceeds n, at which point the base case is reached and the recursion stops.
```python
def print_numbers_recursively(m, n):
    if m > n:  # base case
        return
    print(m)
    print_numbers_recursively(m + 1, n)  # recursive call

print_numbers_recursively(10, 20)
```
### 2. Print Factorial of a Number
Calculating the factorial of a number is a classic example demonstrating the elegance of recursion for solving problems that require repetitive multiplicative steps.

#### Without Recursion (Iterative Approach)
```python
def factorial_iteratively(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```
#### With Recursion
The recursive method multiplies n with the factorial of n-1, progressively breaking the problem down into smaller pieces until it reaches the base case of n = 0 or n = 1.
```python
def factorial_recursively(n):
    if n == 0 or n == 1:  # base case
        return 1
    return n * factorial_recursively(n - 1)  # recursive call

print(factorial_recursively(5))
```
---
# First-Class Functions in Python
- In Python, functions are **first-class citizens**, which means they can be **treated like any other object**. 
- This feature allows for a flexible and expressive programming style. 

### Characteristics of First-Class Functions
Functions in Python exhibit several distinctive properties:
- They can be **assigned to variables**, enabling the use of functions as variable values.
- They are **storable in data structures**, such as lists or dictionaries, facilitating dynamic function management.
- They can be **passed as arguments** to other functions, promoting higher-order function design.
- They can be **returned from other functions**, allowing for complex function composition.

## 1. Assigning Functions to variables
Example:
```python
def greet(name):
    return f"Hello, {name}!"

# Assigning function to a variable
say_hello = greet
print(say_hello("Alice"))  # Output: Hello, Alice!

# Storing functions in a list
function_list = [say_hello, len]
for func in function_list:
    print(func("Python"))  # Output: Hello, Python! and 6
```
In this example:
- `greet` is a regular function that takes a name and returns a greeting string.
- `say_hello` is a variable that is assigned the greet function. 
- **You can now use say_hello as if it were greet.**
- function_list is a list that stores two functions: `say_hello` and `len` (Python's built-in function to get length). 
- We iterate over this list and call each function with the argument "Python".

## 2. Functions stored as list elements
- functions are first-class citizens, meaning they can be passed around, assigned to variables, and stored in data structures just like any other object.
```python
# Define a function to calculate the sum of two numbers and print the result
def sum_numbers(a, b):
    print(a + b)

# Define a function to calculate the difference between two numbers and print the result
def diff_numbers(a, b):
    print(a - b)

# Store the function references in a list
funcs = [sum_numbers, diff_numbers]

# Iterate over the function list and execute each function with arguments (2, 3)
for func in funcs:
    func(2, 3)
```

## 3. Passing Functions as Arguments to Other Functions
- Python allows you to pass functions as arguments to other functions. 
- This is a powerful feature that enables writing high-order functions, functions that take other functions as arguments, or return them as results.
```python
def apply_function(func, value):
    """Applies the function `func` to the `value`."""
    return func(value)

def square(x):
    """Returns the square of x."""
    return x * x

def cube(x):
    """Returns the cube of x."""
    return x * x * x

# Using `apply_function` with different functions
result_square = apply_function(square, 5)  # Output: 25
result_cube = apply_function(cube, 3)      # Output: 27

print(result_square)  # 25
print(result_cube)    # 27
```
In this example:
- `apply_function` is a **high-order function** that takes another function func and a value value, and applies the function to the value.
- `square` and `cube` are simple functions that compute the square and cube of a number, respectively.
- We then use `apply_function` to apply both square and cube to specific numbers.

**Example: Applying Functions Dynamically**
```python
def apply_function(func, value):
    return func(value)

# Using `apply_function` with different functions
result_square = apply_function(lambda x: x * x, 5)
result_cube = apply_function(lambda x: x * x * x, 3)

print(result_square)  # Output: 25
print(result_cube)    # Output: 27
```
In this scenario, apply_function acts as a higher-order function, dynamically applying provided functions to given values.

## Inner Functions: Definitions and Scope
- Inner functions are defined within the scope of another function and are not accessible outside their parent function.

Example: Using Inner Functions

```python
def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()

result = outer_function('hello')
print(result)  # Output: HELLO
```

## Closures: Capturing Enclosing Scope
- Closures are a nuanced concept where a nested function retains the context of its creation, even after the outer function has completed execution.

### Understanding Closures
- **Environment:** 
  - A closure occurs when a nested function (inner function) remembers the environment in which it was created. 
  - The environment consists of any variables in the scope where the inner function was created, not in the scope where it is called.

- **Nested Functions:** 
  - Closures involve a nested function: a function defined inside another function.

- **Persistence of the Outer Function's Local State:** 
  - The outer function has finished executing, but its local variables are not destroyed; they are remembered for use by the inner function.

### Example 1: Basic Closure
- `outer_function` creates a local variable `message` and defines a `inner_function`.
- `inner_function` prints the `message` variable. It doesn't have its own `message`, so it uses the one from the `outer_function`.
- `outer_function` returns `inner_function`. 
- `my_func` is now equal to `inner_function`, but with the `message` variable from outer_function remembered.
- Even after we exit outer_function, the call `my_func()` can still access the message variable that was defined in outer_function.
```python
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

my_func = outer_function('Hello')
my_func()
```
### Example 2: Closure as Factory Functions
- Factory functions are functions that return new, specialized functions. 
- They can be used to create configurations or to encapsulate behaviors that need to be reused with slight variations.
```python
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

say_hello = outer_function('Hello')
say_hi = outer_function('Hi')

say_hello()  # Hello
say_hi()  # Hi
```
```python

def power(exponent):  # This is the factory function
    def base(base_number):  # This is a new function created each time factory is called
        result = base_number ** exponent 
        return result
    return base

square = power(2)
cube = power(3)

print(square(4))  # Outputs: 16
print(cube(4))   # Outputs: 64
```
- In this example, `power_factory` is a factory that **produces functions**. 
- When you call `power_factory(2)`, it creates a new function that squares its input. 
- When you call `power_factory(3)`, it creates a new function that cubes its input. 
- Each function remembers the value of exponent that was used when it was created.

```python
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

print(times3(9))  # Output: 27
print(times5(3))  # Output: 15
```
- In this instance, times3 and times5 are closures, retaining the value of n from their respective creation environments.

---
### Interview Questions
#### Lambda Functions
1. Basic Understanding: Can you explain what a lambda function is and how it differs from a regular function in Python?
2. Practical Usage: Provide an example of how you might use a lambda function in a real-world scenario. When would you prefer a lambda function over a named function?
3. Limitations: Are there any limitations or drawbacks to using lambda functions? Can you discuss a scenario where using a lambda function might not be the best choice?
#### Recursion
1. Conceptual Understanding: Can you explain what recursion is and how it works? Provide an example of a simple recursive function.
2. Efficiency Considerations: Discuss the potential drawbacks of using recursion. What are stack overflows, and how do they relate to recursive calls?
#### First-Class Functions
1. Definition and Implications: Define what a first-class function is. How does treating functions as first-class citizens affect the way you can code in a language?
2. Higher-Order Functions: Provide an example of a higher-order function and explain how it leverages the concept of first-class functions.
3. Use Cases and Benefits: Can you discuss a scenario where first-class functions provide a significant advantage or allow for more elegant code?
#### Closures
1. Basic Understanding: Explain what a closure is in the context of Python. Provide a simple example.
2. Practical Usage: Discuss a practical use case for closures. When would using a closure be more beneficial than other alternatives?
#### Factory Functions
1. Definition and Usage: What is a factory function, and how is it typically used? Provide an example.
---
### Coding Assignments
1. Data Transformation: Write a program that uses lambda functions to transform a list of numbers (e.g., convert temperatures from Celsius to Fahrenheit, find the square of each number).
2. Fibonacci Sequence: Implement a recursive function to compute the Nth number in the Fibonacci sequence.
3. Function as Argument: Write a function that takes another function as an argument and applies it to a list of inputs.
4. Function Returning Function: Implement a function that returns another function, demonstrating the concept of first-class functions.
5. Counter Function: Write a closure that creates a counter function. Each time the counter is called, it should return an incremented value.
6. Write a program to traverse a dictionary with an unknown level of nesting and print each key-value pair.