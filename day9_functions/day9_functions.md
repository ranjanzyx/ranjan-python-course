# Function Basics
## 1. Understanding What a Function Is
- In programming, a function is a block of organized, reusable code that is used to perform a single, related action. 
- Functions provide better modularity for your application and a high degree of code reusing.
- Key Points:
  - **Modularity:** You can encapsulate code as a function and reuse it.
  - **Maintenance:** Functions make the code more organized and manageable.
  - **Reusability:** Once a function is defined, it can be used throughout your code or even in other Python programs.

## 2. Defining Functions Using `def`
- In Python, a function is defined using the `def` keyword. The basic syntax is:
```python
def function_name(parameters):
    """docstring"""
    statement(s)
```
- **function_name:** The name of the function. It follows the same rules of writing identifiers in Python.
- **parameters:** (Optional) They are the values passed into the function.
- **docstring:** (Optional) A brief description of what the function does.
- **statements:** The block of code that the function will execute.

## 3. Calling Functions and Passing Parameters
- Once a function is defined, you can call it from another function, program, or even the Python prompt. 
- To call a function, use the function name followed by parentheses.


- **Parameters**: Are variables that are used in the function definition.
- **Arguments**: Are the values passed into the function call. 
  1. **Positional Arguments:** Values passed into a function in a specific order.
  2. **Keyword Arguments:** Values passed into a function by explicitly stating which parameter they are for.
  3. **Default Arguments:** Default values for parameters if no arguments are provided.

## 4. The `return` Statement
- The `return` statement is used to exit a function and go back to the place where it was called. 
- This statement can contain an expression which gets evaluated and the value is returned. 
- If there is no expression in the statement or the return statement is not present, the function will return `None`.

Key Points:
- **Exiting a Function:** return will immediately terminate the function.
- **Returning a Value:** The function can return data as a result.

## Explanation with code
- **Defining the Function:** add_numbers is defined with two parameters, a and b.
- **Docstring:** The string right after the function header describes what the function does.
- **Adding Numbers:** Inside the function, a and b are added.
- **Returning the Result:** The sum is returned to the caller with return sum_numbers.
- **Calling the Function:** add_numbers(10, 15) calls the function with 10 and 15 as arguments.
- **Printing the Result:** The result of the function call is stored in result and printed.
```python
# Defining a function
def add_numbers(a, b):
    """
    This function adds two numbers and returns the result.
    :param a: first number
    :param b: second number
    :return: sum of a and b
    """
    sum_numbers = a + b  # Adding the numbers
    return sum_numbers  # Returning the sum

# Calling the function and passing parameters
result = add_numbers(10, 15)

print("The result is:", result)  # Output: The result is: 25
```
---
# Parameter Arguments
## 1. Positional Arguments:
- Positional arguments are arguments that need to be included in the correct order. 
- The first parameter defined in a function will be the first argument passed to it, the second parameter will be the second argument, and so on.
```python
def greet(name, greeting):
    """Function to greet a person with a greeting"""
    return f"{greeting}, {name}!"

# Positional arguments
result = greet("Alice", "Hello")
print(result)  # Output: Hello, Alice!
```
In this example, "Alice" is the first argument (for the name parameter), and "Hello" is the second argument (for the greeting parameter).

## 2. Keyword Arguments:
- Keyword arguments are arguments passed to a function, preceded by an identifier. 
- This means you can specify which parameter you want to set, without having to adhere to the order they are defined in the function.
```python
# Same function as before
def greet(name, greeting):
    """Function to greet a person with a greeting"""
    return f"{greeting}, {name}!"

# Keyword arguments
result = greet(greeting="Hello", name="Bob")
print(result)  # Output: Hello, Bob!
```
- In this example, we are explicitly telling the function which parameter each argument corresponds to. 
- This makes the code more readable and allows us to switch the order of arguments.

## 3. Default Parameter Values:
- You can define a default value for a parameter. 
- If the caller does not provide a value for this parameter, the default value is used.
```python
def greet(name, greeting="Hi"):
    """Function to greet a person with a greeting, default is 'Hi'"""
    return f"{greeting}, {name}!"

# Using default parameter value
result1 = greet("Charlie")
print(result1)  # Output: Hi, Charlie!

# Overriding default parameter value
result2 = greet("Charlie", greeting="Hello")
print(result2)  # Output: Hello, Charlie!
```
- In this example, greeting has a default value of "Hi". 
- If no second argument is provided, "Hi" will be used. 
- If a second argument is provided, it will override the default value.

### Notes on Default Arguments:
- Default arguments are evaluated when the function is defined, not when it is called. 
- This can lead to unexpected behavior when using mutable default arguments like lists or dictionaries.
- Always define default parameters at the end of the parameter list to avoid errors related to incorrect positional arguments.
- By combining these concepts, you can create flexible and user-friendly functions.

### Default Arguments are Evaluated at Definition Time
- When a function is defined, the default arguments are evaluated only once, not each time the function is called. 
- This means that if you use a mutable default argument and modify it inside the function, the default value is modified for all subsequent calls to the function. 
- This is contrary to what some might expect, where the default value is reset every time the function is called.
```python
def append_to_list(value, my_list=[]):
    """Appends a value to a list. If no list is provided, appends to a default list."""
    my_list.append(value)
    return my_list

result1 = append_to_list(1)
print(result1)  # Output: [1]

result2 = append_to_list(2)
print(result2)  # Output: [1, 2], might be expected to be just [2]
```
In this example, result2 shows [1, 2] instead of [2] because the same list (my_list) is used across all calls where the list is not provided.

### Recommended Pattern for Mutable Default Arguments
- A common practice to avoid this issue is to use None as the default value and then check for it inside the function to create a new list if needed:
```python
def append_to_list(value, my_list=None):
    """Appends a value to a list. Creates a new list if none is provided."""
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

result1 = append_to_list(1)
print(result1)  # Output: [1]

result2 = append_to_list(2)
print(result2)  # Output: [2], as expected
```

### Default Parameters at the End
- It's a convention (and for a good reason) to define default parameters at the end of the parameter list. 
- This is because positional arguments need to match up with the parameters in the order they are defined. 
- If you have a default parameter before a non-default parameter, you will run into syntax errors or need to use keyword arguments to overcome this, which can make the function calls unnecessarily verbose or confusing.
```python
Copy code
# Incorrect
def func(a=5, b):
    return a + b

# Correct
def func(b, a=5):
    return a + b
```
- In the first example, you will get a syntax error because non-default argument b follows default argument a. 
- In the second example, it's structured correctly, and you can call func(10) which will return 15, assuming the default value of a as 5.
---
# Function Call Mechanics
## _Mutable = passed by reference_
## _Immutable = passed by value_
## 1. Call by Value
- In the Call by Value method, the actual value of an argument is passed to the function. 
- In other words, a **copy of the value is made and passed to the function**. 
- Changes made to the argument inside the function do not reflect in the original value outside the function.

Characteristics:
- **Safety:** The original value is protected from modifications inside the function.
- **Memory Usage:** May consume more memory as copies of variables are created.
- **Performance:** Copying large or complex data structures can be costly in terms of performance.

```python
def modify_value(x):
    x = 10
    print("Inside Function:", x)
    
a = 5
modify_value(a)
print("Outside Function:", a)

# Output
# Inside Function: 10
# Outside Function: 5
```
The variable `a` remains unchanged outside the function, showing that the function interacted with a copy of a.

## 2. Call by Reference
- In the Call by Reference method, instead of passing a copy of the variable, a reference to the original variable is passed. 
- This means that changes made to the parameter affect the passed argument.

Characteristics:
- **Efficiency:** More memory and time-efficient as it doesn't require copying large amounts of data.
- **Risk:** The original data can be modified, which might not be desirable in all cases.

_**Python doesn't have the traditional call by reference, but it behaves similarly when dealing with mutable objects like lists or dictionaries.**_
```python
def modify_list(lst):
    lst.append(4)
    print("Inside Function:", lst)
    
my_list = [1, 2, 3]
modify_list(my_list)
print("Outside Function:", my_list)

# Output:
# Inside Function: [1, 2, 3, 4]
# Outside Function: [1, 2, 3, 4]
```
- The `my_list` is modified inside the function, and the changes are reflected outside as well, showing a behavior similar to call by reference.

## 3. Call by Object Reference (Python's Actual Model)
- Python's model of passing arguments is neither "call by value" nor "call by reference," but rather a hybrid model often referred to as **"call by object reference."** 

- When a function is called, the arguments are passed as references to the actual objects, not as copies of the objects.
- Whether the actual object that the reference points to can be modified or not depends on its type:
  - If the object is immutable (e.g., integer, string, tuple), it behaves like call by value. You can't change the object itself, but you can reassign the reference to a different object.
  - If the object is mutable (e.g., list, dictionary, set), it behaves like call by reference. Changes to the object will be reflected outside the function because the reference points to the original object.
---
# Function Scope
## 1. Local vs. Global Scope
- In Python, variables that are defined inside a function are said to have a local scope. 
- Local scope refers to variables that are accessible only within the function in which they are declared. 
- On the other hand, variables that are defined outside of any function have a global scope.

**Local Scope Example:**
```python
def my_function():
    # local variable
    a_local_variable = 10
    print(a_local_variable)  # prints 10

my_function()
print(a_local_variable)  # This will raise an error, as the variable is not accessible outside the function.
```

**What is wrong with this code ?**
```python
# global variable
a_global_variable = 20

def my_function():
    # The global variable can be accessed inside this function
    print(a_global_variable)  # prints 20
    # a_global_variable = a_global_variable + 1  # ERROR 
    
my_function()
print(a_global_variable)  # prints 20
```
- When you try to print a_global_variable inside my_function, Python finds it in the global scope, so it prints 20 without any issues.
- However, the line `a_global_variable = a_global_variable + 1` raises an error because of the way Python handles variable scopes. 
- **When you assign a value to a variable inside a function, Python considers it a local variable unless explicitly declared as global.** 
- So, when you try to modify `a_global_variable` inside the function by doing `a_global_variable + 1`, Python treats a_global_variable as a local variable. But since it's being referenced before it's assigned, Python doesn't know that a_global_variable should refer to the global variable you've defined outside the function.
- To fix this, you can use the `global` keyword to explicitly tell Python that you want to use the global a_global_variable. 

**Global Scope Example:**
```python
a_global_variable = 20

def my_function():
    global a_global_variable  # Declare that we are using the global variable
    print(a_global_variable)  # prints 20
    a_global_variable = a_global_variable + 1  # Modifies the global variable

my_function()
print(a_global_variable)  # prints 21
```

## 2. LEGB Rule
- **LEGB** stands for Local, Enclosing, Global, Built-in. 
- When you reference a variable in an expression, Python will search these scopes in the LEGB order to resolve the reference.


- **Local (L):** The names that are defined within a function. Function parameters are also in the local scope.
- **Enclosing (E):** The names in the local scope of any and all statically enclosing functions, from inner to outer.
- **Global (G):** The names defined at the top level of a module or declared global in a def within the file.
- **Built-in (B):** The names preassigned in the built-in names module like range, syntax error, etc.

**LEGB Example:**
```python
x = 'global x'  # Global scope


def outer():
    x = 'outer x'  # Enclosing scope

    def inner():
        x = 'inner x'  # Local scope
        print(x)  # inner_x

    inner()
    print(x)  # outer_x


outer()
print(x)  # global x

```
---
# *args & **kwargs
- In Python, `*args` and `**kwargs` are used in function definitions to allow the function to accept a variable number of positional and keyword arguments respectively. 
- This can be particularly useful when you don't know in advance how many arguments will be passed to your function.

## *args
- `*args` allows a function to accept any number of positional arguments.
- It is used when you want your function to be flexible about the number of arguments it can accept.
- **Inside the function, args is a tuple of the passed positional arguments.**

## **kwargs
- `**kwargs` allows a function to accept any number of keyword arguments.
- It is used when you want your function to accept named arguments not explicitly defined in your function signature.
- **Inside the function, kwargs is a dictionary of the passed named arguments.**

#### Example with *args
```python
# A function that uses *args to take in a variable number of arguments
def add_numbers(*args):
    total = 0
    # args is a tuple
    for number in args:
        total += number
    return total

# Can be called with any number of arguments
print(add_numbers(1, 2))  # Output: 3
print(add_numbers(1, 2, 3, 4, 5))  # Output: 15
```

#### Example with **kwargs
```python
# A function that uses **kwargs to accept variable number of keyword arguments
def introduce_yourself(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")

# Can be called with any number of keyword arguments
introduce_yourself(name="John", age=25, country="USA")
# Output:
# name is John
# age is 25
# country is USA
```

#### Combined Example with *args and **kwargs
```python
# A function that accepts any number of positional and keyword arguments
def register_player(*args, **kwargs):
    print("Player's Details:")
    # Handling args
    for arg in args:
        print(arg)
    # Handling kwargs
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function
register_player("John Doe", 30, team="Warriors", position="Forward")
# Output:
# Player's Details:
# John Doe
# 30
# team: Warriors
# position: Forward
```
- In the combined example, `register_player` function can accept any number of positional arguments (*args) and any number of keyword arguments (**kwargs).

#### Combined example with normal positional arguments, default parameters, *args, and **kwargs.
```python
def create_profile(name, age, *hobbies, country="Unknown", **additional_info):
    """
    This function creates a user profile. It requires a name and age, and it accepts
    an arbitrary number of hobbies (positional arguments),
    a country (default argument), and additional named details (keyword arguments).
    """
    print(f"Name: {name}")
    print(f"Age: {age}")
    
    # Handle hobbies (*args)
    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f"- {hobby}")
    else:
        print("No hobbies listed.")

    # Handle country (default parameter)
    print(f"Country: {country}")
    
    # Handle additional information (**kwargs)
    if additional_info:
        print("Additional Information:")
        for key, value in additional_info.items():
            print(f"{key}: {value}")
    else:
        print("No additional information provided.")

# Function call with various arguments
create_profile(
    "Jane Doe", 28,
    "Reading", "Hiking",  # These are *args (hobbies)
    country="Canada",     # This is a default argument override
    occupation="Engineer", education="Bachelor's"  # These are **kwargs
)
```

###  Importance of Ordering
- The ordering is important because it defines how the function interprets the provided arguments when it's called. 
- Here's why each type of argument is placed in this specific order:
1. **Standard Positional Arguments:** 
   - These come first because they are mandatory. 
   - The function expects them in the exact order you define.
2. ***args for Variable Positional Arguments:** 
   - This comes after standard positional arguments because it collects all remaining positional arguments. 
   - If placed before, it would consume all the arguments, and none would be left for the standard positional or keyword arguments.
3. **Keyword Arguments:** 
   - These follow `*args` because they are identified by keywords and not by position. 
   - They must be defined after *args to ensure that all positional arguments (standard and variable) are processed first.
4. #### **kwargs for Variable Keyword Arguments: 
   - This comes last because it's designed to collect any remaining keyword arguments. 
   - If it were placed before any keyword arguments, those keyword arguments would not receive the values passed to them, as **kwargs would have consumed them.


## Keyword only argument
- In Python, you can use a bare `*` in function definitions to indicate that certain arguments must be passed as keyword arguments. 
- This is a feature that enhances the clarity and readability of function calls, especially when the function has a lot of parameters or default values.

### Purpose of Bare *:
- It doesn't capture any arguments itself.
- It signifies that all subsequent parameters in the function definition must be explicitly passed as keyword arguments, not positional arguments.

```python
def function(arg1, arg2, *, kwarg1, kwarg2):
   # Function body...
```
In this definition:
- `arg1` and `arg2` are standard positional arguments.
- `*` signifies that all the parameters following it must be specified as keyword arguments.
- `kwarg1` and `kwarg2` are keyword-only arguments, with default1 and default2 as their default values respectively.

Example:Function Definition:
```python
def calculate_area(length, width, *, print_dimensions):
    area = length * width
    if print_dimensions:
        print(f"The dimensions are {length} x {width}")
    return area
```
In this function:
- `length` and `width` are positional arguments.
- `print_dimensions` is a keyword-only argument due to the presence of *.
Correct Usage:
```python

# Area calculation with dimensions printing
area = calculate_area(10, 5, print_dimensions=True)

# Error: calculate_area() missing 1 required keyword-only argument: 'print_dimensions'
# area = calculate_area(10, 5) 

# This call will result in an error because print_dimensions is passed as a positional argument
# Error: calculate_area() takes 2 positional arguments but 3 were given
# calculate_area(10, 5, True)
```

## Positional-Only Parameters (/) 
- Introduced in Python 3.8, the / symbol in a function definition indicates that parameters before the / are positional-only. 
- This means they cannot be passed as keyword arguments.

Syntax and Usage:
```python
def function(pos1, pos2, /, pos_or_kwarg, *, kwarg):
    # pos1 and pos2 are positional-only.
    # pos_or_kwarg can be positional or keyword.
    # kwarg is keyword-only.
```

### Combining Both in a Function:
- You can use both `/` and `*` in a single function definition to enforce that some parameters are strictly positional, while others are strictly keyword.

Example:
```python
def function(pos1, pos2, /, pos_or_kwarg, *, kwarg1, kwarg2):
    # pos1 and pos2 are positional-only.
    # pos_or_kwarg can be positional or keyword.
    # kwarg1 and kwarg2 are keyword-only.
```
In this example:
- pos1 and pos2 must be provided as positional arguments and cannot be provided as keyword arguments.
- pos_or_kwarg can be provided either as a positional or a keyword argument.
- kwarg1 and kwarg2 must be provided as keyword arguments.

### Example Function: Planning an Event
- Positional-only arguments: date and time (these should not be named when calling the function)
- Arguments that can be positional or keyword: venue
- Keyword-only arguments: catering and equipment (these must be named when calling the function)
```python
def plan_event(date, time, /, venue, *, catering, equipment):
    print(f"Event Date: {date}")
    print(f"Event Time: {time}")
    print(f"Venue: {venue}")
    print(f"Catering Service: {catering}")
    print(f"Equipment: {equipment}")
```
Calling the plan_event Function:
```python
plan_event("2024-01-30", "18:00", "Grand Hall", catering="Gourmet Catering", equipment="Audio System")
plan_event("2024-01-30", "18:00", venue="Grand Hall", catering="Gourmet Catering", equipment="Audio System")

# Error
# plan_event() got some positional-only arguments passed as keyword arguments: 'time'
# plan_event("2024-01-30", time="18:00", venue="Grand Hall", catering="Gourmet Catering", equipment="Audio System")  
```
Explanation:
In this example:
- date and time are positional-only due to the / after them in the function definition. They must be provided positionally and cannot be named when calling the function.
- venue is between / and *, so it can be provided either positionally or as a keyword argument.
- catering and equipment are keyword-only arguments due to the bare * before them in the function definition. They must be named when calling the function.
---
# Docstrings
- **Docstrings** in Python serve as documentation for your code. 
- They are placed right inside the function, class, or module you are documenting and are enclosed in triple quotes. 
- Python's `help()` function can read these docstrings to provide a helpful summary of the component. 
- Docstrings are not only useful for others reading your code, but also for you when you return to your code after some time.

**1. One-liner Docstring:**
```python
def add(a, b):
    """Return the addition of two numbers."""
    return a + b
```
**2. Multi-line Docstring:**
```python
def add(a, b):
    """
    Return the addition of two numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of the two numbers.
    """
    return a + b
```
When writing multi-line docstrings, it's common to include sections such as:
- **Short description:** A brief summary of what the function does.
- **Parameters/Arguments:** Description of the function's arguments.
- **Returns/Result:** Description of what the function returns.
- **Raises:** Description of any errors or exceptions that might be raised.


## Types of Docstrings
1. **PEP 257 - Python's Standard Docstring Convention:** 
  - This is the original docstring convention recommended by Python's Enhancement Proposal 257 (PEP 257). 
  - It focuses on conventions such as how multi-line docstrings should be formatted, how to handle quotes, and the content of docstrings.
```python
def function(arg1, arg2):
    """
    Summary of the function.

    More detailed description.

    :param arg1: Description of arg1
    :param arg2: Description of arg2
    :return: Description of return value
    """
    return something
```
2. **Google Style Docstrings:** 
  - This style is widely used and favored for its readability, especially when it comes to documenting functions with parameters and return values.
  - It uses a more structured format, making it easy to read and write, especially for complex functions.
```python
def function(arg1, arg2):
    """
    Summary of the function.

    More detailed description.

    Args:
        arg1 (int): Description of arg1.
        arg2 (str): Description of arg2.

    Returns:
        bool: Description of return value.
    """
    return something
```
3. **NumPy/SciPy Docstrings:** 
  - This style is commonly used in scientific and mathematical Python communities, notably within the NumPy and SciPy projects. 
  - It's very detailed and well-suited for documenting complex code.
```python
def function(arg1, arg2):
    """
    Summary of the function.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value
    """
    return something
```
---
# Type Hints
- Type hints and annotations in Python enhance the readability and maintainability of code. 
- They allow developers to explicitly state the expected types of variables, function parameters, and return values. 
- The `typing` module, introduced in **Python 3.5**, provides support for type hints.

## Using Type Hints for Function Parameters and Return Types
- Type hints can be added to function parameters and return types using the colon (:) and arrow (->) syntax, respectively.
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

In this function:
- **name: str** indicates that the name parameter should be of type string.
- **-> str** indicates that the return type of the greet function is a string.

## The `typing` Module
- The typing module provides support for more complex types, such as List, Dict, Union, Optional, and many others.

### 1. List, Set, Dict, Tuple:
```python
from typing import List, Set, Dict, Tuple

def process_values(values: List[int]) -> None:
    print(values)

def coordinates() -> Tuple[int, int, int]:
    return (1, 2, 3)
```
### 2. Optional:
Indicate that a variable can be of a specified type or None.
```python
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, guest!"
    else:
        return f"Hello, {name}!"
```
### Union:
Allow a variable to be one of multiple types.
```python
from typing import Union

def process_input(value: Union[int, str]) -> None:
    print(value)
```
### Callable:
Specify that a variable is a callable (like a function) and its signature.
```python
from typing import Callable

def execute(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
```
```python
from typing import Callable

# Define callable types for different operations
AddOperation = Callable[[int, int], int]
SubtractOperation = Callable[[int, int], int]

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

# Executor function that takes a callable (operation) and two integers
def execute(operation: Callable[[int, int], int], a: int, b: int) -> int:
    result = operation(a, b)
    print(f"The result of the operation is: {result}")
    return result

# Using the executor with different operations
execute(add, 10, 5)          # Output: The result of the operation is: 15
execute(subtract, 10, 5)     # Output: The result of the operation is: 5
```

---

## Interview Questions
1. What is a function in programming, and why are functions important?
2. How does Python differentiate between positional, keyword, and default arguments in a function? Provide examples.
3. Illustrate with examples and explain the significance of the function definition order: positional arguments, *args, keyword arguments, and **kwargs.
4. Can you explain the difference between local and global scope? What are the implications of variable shadowing?
5. Discuss how Python's scope resolution works (LEGB rule) and the use of the global and nonlocal keywords.
7. How does Python handle mutable and immutable objects as function arguments? Can you explain the term "call by object reference"?
8. Discuss the difference in behavior when passing mutable (like lists) and immutable (like integers and strings) objects to a function.
9. What are docstrings, and how do they improve code readability and maintenance?

## Assignments

1. Calculator Functions: 
   - Create a calculator that can perform addition, subtraction, multiplication, and division. 
   - Each operation should be defined in its own function.
   - Implement a function for each operation: add(a, b), subtract(a, b), multiply(a, b), and divide(a, b).
   - Ensure that the divide function handles division by zero by raising an appropriate error.
2. Temperature Converter: 
   - Write a function convert_temperature that converts a temperature from Fahrenheit to Celsius and vice versa. 
   - The function should have a default argument indicating the unit of the input temperature.
   - Function signature: convert_temperature(temp, unit='C')
   - If unit is 'C', convert from Celsius to Fahrenheit; if unit is 'F', convert from Fahrenheit to Celsius.
3. Dynamic Itemized Bill Generator: 
   - Create a function generate_bill that takes a restaurant order and generates an itemized bill. 
   - The function should be able to handle an arbitrary number of items and their prices.
   - Use *args to accept the item names and **kwargs for the price of each item.
   - The function should return the total cost and optionally print the itemized bill if a certain keyword argument, like print_bill=True, is provided.
