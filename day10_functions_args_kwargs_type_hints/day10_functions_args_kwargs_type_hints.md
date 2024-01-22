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
6. What is recursion, and how does it differ from iterative solutions? Can you provide an example where recursion is the most suitable approach?
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
