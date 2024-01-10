## Introduction
- Welcome to Day 3 of our Python course! 
- Today, we'll dive into the essentials of Python programming: variables, constants, enums, basic operators, and handling input/output. 
- These concepts are fundamental to building any Python program.
---

## Expressions and Statements in Python
- Python, like many programming languages, uses two primary kinds of syntax: `expressions` and `statements`. 
- Understanding the difference between these two is essential for writing clear and efficient Python code.

### Expressions
- An expression in Python is any valid unit of code that **resolves to a value**. 
- Expressions are combinations of values and functions that are evaluated by the interpreter to produce another value. 
- They can be simple, involving just values and operators, or complex, involving function calls.
- Examples of Expressions:
  - Arithmetic Expression: An expression that performs arithmetic operations.
  - String Concatenation: Combining string values using the + operator.
  - Function Calls: Calling a function and evaluating to its return value.
```python
5 + 3 * 2  # Arithmetic expression
"Hello, " + "world!"  # String expression
len("Python")  # Function expressions
```

### Statements
- A statement in Python, on the other hand, is an instruction that the Python **interpreter can execute**. 
- While expressions are primarily about producing values, statements are about performing actions. 
- Each statement corresponds to a command or an action. 
- Examples include declaring a variable, printing a value, or running a loop.
- Examples of Statements:
  - Assignment Statement: Assigns a value to a variable.
  - Print Statement: Outputs a value to the console.

```python
x = 10  # Assignment Statement
print("Hello, Python!")  # Print Statement
```
---
## Variables in Python
- Variables are symbols that store data in a program. 
- Their content can change, hence the name 'variables'.

**Creating and Using Variables:**
```python
# Creating variables
age = 25
name = "Alice"

# Using variables
print(name, "is", age, "years old.")  # Output: Alice is 25 years old.
```
### Variable Naming Conventions 
- In Python, variable naming conventions are important to make your code more readable and maintainable. 
- Following these conventions helps ensure that your code is consistent and easily understood by other developers. 
- Here are some common variable naming conventions in Python:
  - **Snake Case:** 
    - Snake case is the most common naming convention for variables in Python. 
    - It involves using lowercase letters and separating words with underscores. For example:
      - `my_variable`, `user_name`, `num_of_elements`
  - **Camel Case:** 
    - Camel case is used for naming variables, especially in situations where you want to mimic the style of other programming languages. 
    - It involves starting each word with a capital letter and no spaces or underscores between words. For example:
      - `myVariable`, `userName`, `numOfElements`
  - **Pascal Case:** 
    - Pascal case is similar to camel case but starts with a capital letter. 
    - It is often used for naming classes or objects in Python. For example:
      - `MyClass`, `UserData`, `NumOfElements`
  - **UPPER_CASE:** 
    - When you have constants or global variables, it is common to use all uppercase letters with underscores to separate words. For example:
      - `PI`, `MAX_VALUE`, `API_KEY`
  - **Single Underscore Prefix:** 
    - A single underscore prefix is often used to indicate that a variable or method is intended to be "protected" or non-public. 
    - It's a convention to signal to other developers that they should not access these variables or methods directly. For example:
      - `_private_variable`, `_protected_method`
  - **Double Underscore Prefix:** 
    - A double underscore prefix is used for **name mangling** in Python. 
    - It changes the way the variable is stored in the instance namespace to avoid conflicts with subclasses. For example:
      - `__private_variable`
  - **Leading Underscore and Trailing Underscore:** 
    - A leading underscore is sometimes used to indicate that a variable is intended for internal use within a module or package. 
    - A trailing underscore is sometimes used to avoid conflicts with Python keywords or built-in names. For example:
      - `_internal_variable`, `class_`
  - **Descriptive Names:** 
    - Use descriptive and meaningful names for your variables to make your code self-explanatory. 
    - This enhances code readability. For example:
      - `total_sales` instead of `ts`
      - `user_input_text` instead of `uit`
  - **Avoid Using Single Letters:** 
    - Unless a variable is an iterator in a loop, avoid using single-letter variable names like `i`, `j`, or `k`. 
    - Instead, use more descriptive names that convey the purpose of the variable.

### Types of Variables:
- **Local Variables:** 
  - These are defined inside a function and can only be used within that function. 
  - They are not accessible outside the function.
  ```python
  def local_example():
      local_var = "I am a local variable"
      print(local_var)  # This will print the local variable
  
  # Trying to print local_var outside the function will result in an error
  # print(local_var)  # Uncommenting this line will cause an error
  ```
- **Global Variables:** 
  - These are defined outside of any function and can be accessed from anywhere in the code, both inside and outside of functions.
  ```python
  global_var = "I am a global variable"
  def global_example():
      # Here we can access the global variable
      print(global_var)  

  # The global variable is also accessible outside the function
  print(global_var)
  ```
- **Nonlocal Variables:** 
  - These are used in nested functions and allow us to assign a value to a variable in the nearest enclosing scope (other than the global scope).
  ```python
  def outer_function():
      outer_var = "I am in the outer function"

      def inner_function():
          nonlocal outer_var
          outer_var = "Modified by inner function"

    inner_function()
    print(outer_var)  # This will print "Modified by inner function"

  outer_function()
  ```
  - In this nonlocal example, `outer_var` is defined in `outer_function`. 
  - Inside inner_function, we use `nonlocal` to declare that `outer_var` refers to the one defined in `outer_function`, and then we modify it. 
  - The change is reflected when we print `outer_var` in `outer_function` after calling `inner_function`.

### Variable Assignment and Memory Management
#### Immutable vs Mutable
- In Python, **everything is an object**, including numbers, strings, functions, classes, and even modules.
- Objects can be immutable (like integers, floats, strings, tuples) or mutable (like lists, dictionaries, sets). 
- Immutable objects can't be changed after they are created, while mutable objects can be modified.
```python
# Immutable objects - integers, floats, strings, tuples
x = 10
# Print the memory address of the variable x.
# This is where the integer 10 is stored.
# Immutable objects like integers cannot be altered once created.
print(id(x))  # Example Output: 140725799369432

# When we modify the value of x, Python creates a new integer object.
# Here, we're not altering the integer 10, but rather creating a new integer 11.
x = x + 1
# Print the memory address of the new value of x.
# Note that this address is different from the previous one,
# indicating that a new object has been created.
print(id(x))  # Example Output: 140725799369464

# Mutable objects - lists, dictionaries, sets
y = [10]
# Print the memory address of the list y.
# This address points to the list object, which can be modified.
print(id(y))  # Example Output: 2445974622592

# Append a new element to the list.
# Unlike immutable objects, we can change lists without creating a new object.
# Here, we add the integer 11 to the list, but the list itself remains the same object.
y.append(11)
# Print the memory address of the list y again.
# Notice that the address is the same as before, indicating the same list object has been modified.
print(id(y))  # Example Output: 2445974622592
```
#### Assignment Creates References: 
- When you assign a value to a variable, Python creates an object (if it doesn't already exist) and 
- the variable references that object. 
```python
# Assignment and Cloning in Python

# Creating a list with one element.
x = [10]
# Print the memory address of the list x.
# This address is unique to the list object.
print(id(x))  # Example Output: 2066350395776

# Assigning y to x. Here, we're not creating a new list.
# Instead, y becomes a reference to the same list object as x.
y = x
# Print the memory address of y.
# Notice it's the same as x, indicating both x and y refer to the same list object.
print(id(y))  # Example Output: 2066350395776

# Append a new element to the list via x.
# Since y is a reference to the same list, this change is reflected in y as well.
x.append(11)

# Both x and y show the updated list, confirming they reference the same object.
print(x)  # Output: [10, 11]
print(y)  # Output: [10, 11]
# The memory addresses of x and y remain unchanged and identical.
print(id(x))  # Example Output: 2066350395776
print(id(y))  # Example Output: 2066350395776

# Using deepcopy to create an actual copy of the list.
import copy
z = copy.deepcopy(x)
# Print the memory addresses of x, y, and z.
# Notice that z has a different address, indicating it's a completely new list object.
print(id(x))  # Example Output: 2066350395776
print(id(y))  # Example Output: 2066350395776
print(id(z))  # Example Output: 2066350729088

# Append another element to x.
# This change will not affect z, as z is a deep copy and thus a separate object.
x.append(12)
# x and y show the new list, while z remains unchanged.
print(x)  # Output: [10, 11, 12]
print(y)  # Output: [10, 11, 12]
print(z)  # Output: [10, 11]

```
---

## Constants in Python
- In programming, a constant is a type of variable whose **value cannot be changed**. 
- It's a useful way to define values that remain the same throughout the execution of a program, like a maximum size, specific path, or a magic number.

- Python, unlike some other programming languages, doesn't have built-in support for true constants. 
- However, it's a common convention to use **all-uppercase letters** to define a constant, signaling to other programmers that these values should not be changed.
- In the below example, MAX_SIZE and PI are constants and should not be modified in the program.
```python
MAX_SIZE = 100
PI = 3.14159
```

#### Naming Standards for Constants in Python
- In Python, while there's no technical enforcement for constants, there is a widely accepted naming convention:
- **All Uppercase with Underscores:** 
  - Constants are typically defined using all uppercase letters with words separated by underscores. 
  - This makes constants easily distinguishable from regular variables.
```python
# Good practice
MAX_SIZE = 50
DEFAULT_TIMEOUT = 120

# Not recommended
max_size = 50       # Looks like a regular variable
```

## Enums in Python
- Enums (short for Enumerations) are a feature in Python, introduced in version 3.4, that allows you to create a set of named values. 
- An enum is a class that inherits from `enum.Enum`. 
- Each member of the enum is a constant and represents a unique instance of the enum.
#### Naming Standards for Enums in Python
- **Class Name in PascalCase:** The name of the enum class should be in PascalCase (or CapWords)
- **Members in Uppercase:** Similar to constants, the members of an enum are written in uppercase letters, separated by underscores.
```python
from enum import Enum

class HttpStatus(Enum):
    OK = 200
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
```

### How Enums Enforce Constant Values
- Enums in Python help enforce constant values in a couple of ways:
  - **Immutability:** 
    - Once an enum is created, its members cannot be modified or re-assigned. 
    - This makes enums a safe way to declare constants because their values are fixed.
  - **Uniqueness:** 
    - Each member of an enum is guaranteed to be unique within that enum. 
    - This helps avoid accidental re-use or conflict of constant values in your code.

```python
from enum import Enum

class StatusCode(Enum):
    OK = 200
    NOT_FOUND = 404
    ERROR = 500

status = StatusCode.OK
print(status)  # Output: StatusCode.OK
print(status.value)  # Output: 200
status.value = status.value + 1  # AttributeError: <enum 'Enum'> cannot set attribute 'value'
```
- In this example, `StatusCode` is an enum with constant values for HTTP status codes. 
- It's clear what each status represents, and these values cannot be altered.

---
## Basic Operators in Python
### Arithmetic Operators
- Perform mathematical calculations: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `%` (modulus), `**` (exponent), `//` (floor division).
```python
x = 10
y = 3

print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation
print(x // y) # Floor division
```
### Comparison Operators
- Compare two values: `==` (equal), `!=` (not equal), `>` (greater than), `<` (less than), `>=` (greater than or equal to), `<=` (less than or equal to).
```python
a = 5
b = 3

print(a == b)  # Equal
print(a != b)  # Not equal
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to
```
### Logical Operators
- Used to combine conditional statements, includes `and`, `or`, `not`.
```python
a = True
b = False

print(a and b) # Logical AND
print(a or b)  # Logical OR
print(not a)   # Logical NOT
```
### Bitwise and Augmented Assignment Operators
- **Bitwise Operators:** Perform operations on bits: `&` (and), `|` (or), `^` (xor), `~` (not), `<<` (left shift), `>>` (right shift).
- **Augmented Assignments:** Shortcuts like `+=`, `-=`, `*=`, `/=`, etc.


```python
# Augmented assignment example
x = 10
x += 5  # Equivalent to x = x + 5
``` 
---
## Input/Output in Python
### Input in Python:
#### input() function:
- The `input()` function is used to receive input from the user through the console.
- By default, `input()` returns the user's input as a string.
- You can provide a prompt within the input() function to instruct the user on what to enter.
```python
name = input("Enter your name: ")  # Prompt the user to enter their name
age = input("Enter your age: ")    # Prompt the user to enter their age
```
- In the above code, name and age will both contain string values.
- If you need to work with input as other data types like `integers` or `floats`, you can use type casting functions like `int()`, `float()`, etc., to convert the input.
```python
age = int(input("Enter your age: "))  # Convert to integer
```
### Output in Python:
#### print() function:
- The print() function is used to display output to the console.
- You can pass one or more values to print(), separated by commas, and it will print them to the console.
```python
print("Hello, World!")
```
- Printing Variables:
```python
print("Name:", name, "Age:", age)
```
- This will display a message like "Name: John Age: 25" if the user entered "John" for the name and "25" for the age.
---

### Practice Exercises
1. **Create and Manipulate Variables:** Ask the user for their name and age, and then print a message using these variables.
2. **Calculator:** Write a simple calculator that takes two numbers and an operator as input and performs the corresponding operation.

**Interview Questions and Practical Scenarios**
1. **Variable Naming Conventions:** Why can't a variable name start with a number in Python?
2. **Operator Precedence:** What is the order of operations when using multiple operators in a single expression?
3. **Tricky Scenario:** What will be the output of print("5" + 3) and why?

**Conclusion**
- Today, you've learned about variables, basic arithmetic, comparison, and logical operators, along with handling user input and producing output.
- In our next session, we'll cover control flow with if, elif, else, and loops (for and while). This will bring us closer to writing more dynamic and interactive Python programs.