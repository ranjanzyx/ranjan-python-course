## Day 2: Understanding Python execution, Basic Syntax and Data Types
- Today, we delve into 
  - Python's basic execution process 
  - Understand how to write comments
  - Explore fundamental data types such as integers, floats, strings and booleans.

## Understanding Python's Execution Process: From Source Code to Output
```
[1] Writing a Python Script
      |
      |  hello.py
      |  ----------------
      |  print("Hello World")
      |
      v
[2] Compilation to Bytecode 
      |
      |  Python Compiler
      |  ----------------
      |  Converts hello.py to bytecode (OS independent)
      |  (hello.pyc or similar)
      |
      v
[3] Execution by Python Virtual Machine (PVM)
      |
      |  PVM (Specific to each OS)
      |  -------------------------
      |  Interprets the bytecode
      |  Executes the program
      |
      v
[4] Output on User's Device
      |
      |  Console Output
      |  --------------
      |  "Hello, World"
```

### Is Python an Interpreted or Compiled Language?
- Python is often referred to as an interpreted language, but in reality, it's both interpreted and compiled. 
- Here's how it works:
  1. **Compilation:** 
      - When you write a Python program, the source code you write is first compiled into something called bytecode. 
      - This is a lower-level, platform-independent representation of your source code.
  2. **Interpretation:** 
     - This bytecode is then interpreted by the Python Virtual Machine (PVM) to execute the program.

### What is Bytecode?
- Bytecode is a form of instruction set designed for efficient execution by a software interpreter. 
- In the context of Python, after you write a Python program, the source code (.py files) is first compiled into bytecode(.pyc files).
- This bytecode (.pyc files) is not human-readable like the original source code, but it's a set of instructions that the Python interpreter can execute.

### What is the Python Virtual Machine (PVM)?
- The Python Virtual Machine is an interpreter which reads and executes the bytecode. 
- The PVM is the last step in the process of running a Python script.
- It's the PVM that actually runs your Python programs.

### How is Python Platform Independent?
- The beauty of Python's approach lies in its platform independence. 
- When you write Python code, you don't compile it into machine-specific code. 
- Instead, you compile it into Python bytecode, which is the same for every platform.
- Then, each platform (Windows, macOS, Linux, etc.) has its own version of the PVM that understands how to execute this bytecode. 
- So, you write your Python code once, and it can run on any platform that has a Python interpreter.


## Python Basic Syntax
- Python syntax refers to the set of rules that define how a Python program will be written and interpreted (both by the interpreter and by humans).
- Unlike many other programming languages, Python emphasizes readability and simplicity.

---
## Writing Comments in Python
- Comments are essential for making your code more readable.
- Comments start with a **#**, and everything after **#** on that line is ignored by the interpreter.
  1. **Single-line comments** are great for brief **explanations**.
  2. **Multi-line comments** are often used for **documentation** at the beginning of a function or a file.
    ```python 
    """
    This is a multi-line comment.
    Useful for longer descriptions.
    """
    # This is a single-line comment
    ```  
  
- Check the usage of comments in `C:\Users\RANJANZYX\AppData\Local\Programs\Python\Python312\Lib\logging\handlers.py`
- #### Do:
    - Write comments that explain the 'why', 'for what', or 'how' behind complex code segments.
    - Write readable and clear/concise comments as if they are for someone unfamiliar with the code.
- #### Don't:
    - Over-comment simple code; the code should be self-explanatory as much as possible.
    - Write misleading comments.
      ```python
      """
      Title: Sample Python Script
      Author: Ranjan
      Date: January 9, 2024
      Description: This script is  intended as a tutorial for beginners learning Python programming.    
      """

      # DO: Explain complex logic (Why and How)
      def calculate_discount(price, discount):
        """
        Calculate the discounted price of an item.
    
        :param price: float, the original price of the item
        :param discount: float, the discount percentage (0-100)
        :return: float, the price after applying the discount
        """
        # Checking if discount is applicable
        if discount > 0:
            # Applying discount: price * (100 - discount) / 100
            return price * (100 - discount) / 100
        else:
            # Return the original price if no discount is given
            return price
    
      # DON'T: State the obvious
    
      def add(a, b):
        # Adding two numbers
        return a + b  # This comment is unnecessary as the code is self-explanatory
    
      # DON'T: Leave commented-out code in the final version
      def subtract(a, b):
        # Subtracting b from a
        # result = a - b
        # return result
        return a - b  # Clean and concise without the commented-out code
    
      # DON'T: Write misleading comments
      def multiply(a, b):
        # Divide a by b - This comment is incorrect and misleading
        return a * b  # The function actually multiplies a and b
      ```
---
### Indentation
- Python uses **indentation** to define blocks of code, unlike curly braces in languages like C++ or Java. 
- Each block of code under a statement must be indented by the same amount.
- The standard Python convention is to use **four spaces** for each level of indentation.
- Example of Python Syntax:
```python
# Correct Indentation
if 5 > 2:
    print("Five is greater than two!")  # This line is correctly indented

# Incorrect Indentation
if 5 > 2:
print("This will cause an error.")  # This line is not indented
```
---
### Case Sensitivity
- Python is a case-sensitive programming language, which means that it distinguishes between identifiers based on their case.
- This case sensitivity applies to variables, function names, class names, and other identifiers.
- In Python, `number`, `Number`, and `NUMBER` are treated as three distinct variables due to case sensitivity.
- Being case-sensitive, Python requires consistent use of casing in identifiers, which can sometimes lead to errors if not managed carefully.
```python
number = 10
Number = 20
NUMBER = 30
print(number)  # Outputs 10
print(Number)  # Outputs 20
print(NUMBER)  # Outputs 30
```
- In contrast to Python, there are languages where case sensitivity is not maintained, such as **SQL** and **Fortran**.

---
## Python Data Types
![img.png](imgs/img.png)

### What is a datatype ?
- A data type in programming refers to the classification of data which tells the compiler or interpreter how the programmer intends to use the data. 
- Data types define what type of value a variable can hold, such as integer numbers, floating-point numbers, strings, etc. 
- They also determine the operations that can be performed on the data and the way it is stored in memory. 
- The concept of data types is fundamental in programming and is crucial for understanding how to manipulate data effectively in any programming language.

 
Data types are often categorized into two main groups: primitive (or basic) data types and composite (or complex) data types.
1. **Primitive Data Types:** 
   - These are the basic data types that form the building blocks of data manipulation in Python. 
   - They typically represent single values and include types like:
     1. Integer (`int`)
     2. Float (`float`)
     3. String (`str`)
     4. Boolean (`bool`)
     5. NoneType (`None`)
2. **Composite Data Types:** 
   - Also known as complex data types, these are used to store collections or more complex data structures. 
   - They can hold multiple items, possibly of different data types, and include types like:
     1. `List`
     2. `Tuple`
     3. `Set`
     4. Dictionary (`dict`)

---
### Integer (int)
- **Definition:** In Python, an integer is a **whole number**, positive or negative, without a fraction.
- **Range:** 
  - Python integers have **unlimited precision**, meaning they can grow to have as many digits as your memory allows. 
  - There's no fixed upper or lower bound.
- **Common Integer Operations:**
  - Arithmetic Operations: Addition (+), Subtraction (-), Multiplication (*), Division (/), Integer Division (//), Modulus (%)
  - Equal to (==), Not equal to (!=)
  - Greater than (>), Less than (<), Greater than or equal to (>=), Less than or equal to (<=)
```python
x = 6
y = 3

print(x + y)  # Output: 9
print(x - y)  # Output: 3
print(x * y)  # Output: 18
print(x / y)  # Output: 2.0
print(x // y)  # Output: 2
print(x % y)  # Output: 0
```

### Floating Point (float)
- **Definition:** In Python, a float represents real numbers, meaning they can have a **fractional part**. 
- Floats are essential for representing numbers that cannot be expressed as integers, such as measurements, scientific calculations, and more.
- **Precision:** Python floats are typically **64-bit double-precision numbers**, giving them a significant degree of accuracy. 
- For example, 1.2e-5 represents 1.2 times 10 to the power of -5 (0.000012).
- Arithmetic Operations: Addition (+), Subtraction (-), Multiplication (*), Division (/), Exponentiation (**)
- Comparison Operations: floats can be compared using ==, !=, >, <, >=, <=.
- **Precision Issues:** Due to their binary representation, floats can sometimes give unexpected results.
```python
a = 0.1
b = 0.2
c = a + b
print(c)  # Might not output 0.3 exactly due to precision; typical output: 0.30000000000000004
print(round(c, 1))  # Output: 0.3
```
### Boolean (bool)
- **Definition:** In Python, a Boolean (or bool) is a data type that represents one of two values: True or False. 
- Booleans are primarily used in conditional statements, making them a fundamental part of controlling the flow of a Python program.
```python
is_student = True
has_id = False

# Using 'and' logical operator
if is_student and has_id:
  print("Access granted")
else:
  print("Access denied")  # This will be executed

# Using 'not' operator
if not has_id:
  print("ID is required")  # This will be printed
```

### None datatype
- In Python, `None` is a special data type that represents the **absence of a value** or a null value. 
- It is an object of its own datatype, the `NoneType`. 
- None is often used to signify 'nothing' or 'no value here'
```python
# Initializing a variable with None
result = None

# Using None in conditional statements
if result is None:
    print("No result yet.")
    # proceed to calculate values
```
### String (str)
- **Definition:** 
  - A string represents a **sequence** of characters.
  - As a sequence, each character in a string has an index, starting from 0.
  - In Python, strings are enclosed in single ('...') or double ("...") quotes with equivalent functionality.
  - **Quotes:** Single quotes are straightforward for most strings, but double quotes are useful to include apostrophes within the string.
  - **Escape Characters:** To include special characters like apostrophes in single-quoted strings, escape characters (like \) are used.
  - **Multi-line Strings:** Triple quotes ('''...''' or """...""") enable the creation of strings that span multiple lines.
  - **Basic Operations:**
    - Concatenation: Joining strings together (+).
    - Formatting: Embedding values into strings (f-strings or format method).
    - Common Methods: strip(), split(), replace(), upper(), lower(), etc.
  
```python
# Single and Double Quotes
greeting = 'Hello, World!'
word = "Bob's world"  # Useful for apostrophes
word_with_escape = 'Bob\'s world'  # Using escape character

# Multi-line String
multi_line_string = """This is a multi-line string
spanning over several lines."""

print(greeting)
print(greeting[0])
print(greeting.upper())
```
---
## Python Type Conversion and Data Types

### Dynamic Typing in Python
- Python is a dynamically typed language, meaning that the type of a variable is determined at runtime. 
- This flexibility allows for more generalized and concise code, but it also requires careful management of variable types, especially when performing various operations. 
```python
salary = 100
print(type(salary))

hike = 1.5
salary = salary * hike
print(type(salary))

salary = "The final salary is " + str(salary)
print(type(salary))
print(salary)
```

- In statically typed languages like **Java**, 
  - Variables have fixed data types
  - Attempting to change the type or mix types without explicit casting results in a compilation error.
```java
// java
int salary = 100;  // Salary declared as an integer
double hike = 1.5;

// Attempting to directly multiply an int and a double results in an error
salary = salary * hike;  

// Concatenating a string with a non-string requires explicit conversion
String salaryString = "The final salary is " + salary;
```


### Understanding Data Types with the type() Function
- To identify the data type of a variable in Python, the type() function is used. 
- This is especially useful in a dynamically typed language, as it helps confirm assumptions about the type of data you are working with.

- Example Usage:
```python
num = 5
print(type(num))  # Output: <class 'int'>

decimal = 5.0
print(type(decimal))  # Output: <class 'float'>

text = "Python Programming"
print(type(text))  # Output: <class 'str'>
```

### Explicit vs Implicit Type Conversion
- Type conversion in Python can be either explicit or implicit. 
- Explicit conversion, also known as type casting, is when you manually convert one data type to another using conversion functions. 
- Implicit conversion happens automatically when Python interprets one data type as another during operations.

#### Explicit Type Conversion
- Explicit type conversion involves using functions like int(), float(), and str() to convert a variable to a different type.
```python
int_to_float = float(5)    # Converts integer 5 to float (5.0)
float_to_int = int(8.7)    # Converts float 8.7 to integer (8)
int_to_str = str(20)       # Converts integer 20 to string ("20")

invalid_conversion = int("hello") # This will cause an error 
```

#### Implicit Type Conversion
- Python automatically performs implicit type conversion to avoid data loss. 
- This occurs during operations involving multiple data types.
```python
num_int = 123
num_float = 1.23

# Implicit conversion of int to float for addition
num_sum = num_int + num_float
print("Sum:", num_sum)  # Output: Sum: 124.23
```

#### Type Conversion in Debugging
- Understanding and diagnosing data type issues is a critical part of debugging in Python. 
- By using type(), you can identify mismatches in data types and perform appropriate conversions.
- Debugging Example:
```python
x = "123"
y = 456

# Understanding the data types
print("Type of x:", type(x))  # Output: <class 'str'>
print("Type of y:", type(y))  # Output: <class 'int'>

# Converting x to an integer for addition
total = int(x) + y
print("Total:", total)  # Output: Total: 579
```

#### When Type Casting is Essential
- In Python, certain operations require explicit type casting to avoid runtime errors and ensure that the operation behaves as intended. 
- One common scenario is when you need to perform operations that involve both numbers and strings. 
- Since these are fundamentally different data types, Python does not implicitly convert one to the other.
- **Adding a Number to a String**
  - Consider a situation where you need to concatenate a string with a number. 
  - Since concatenation is a string operation, any non-string data type must be explicitly converted to a string.
```python
age = 30
greeting = "Hello, I am "

# Attempting to concatenate a string and an integer directly will result in a TypeError
# full_greeting = greeting + age  # This would cause an error

# Correct approach using explicit type conversion
full_greeting = greeting + str(age)
print(full_greeting)  # Output: Hello, I am 30
```

### Difference between `type()` and `isinstance()` Function:
- The **isinstance()** function checks if an object is an instance of a particular class or a tuple of classes. 
- It's used to check if an object inherits from a certain class or a tuple of classes (directly or indirectly).
```python
x = 10
print(isinstance(x, int))  # Output: True
print(isinstance(x, (float, int)))  # Output: True, as x is an instance of int
```
- Advantage: isinstance() is more flexible than type() because it supports class inheritance, making it suitable for checking an object's compatibility with an interface or abstract class.
- In summary, while type() is used for finding the exact type of an object, isinstance() is used to check if an object is of a specific type or a subclass of that type, making it more suitable in polymorphic scenarios.

## Interview Questions
**1. What is Dynamic Typing in Python?**   
Dynamic typing in Python refers to the ability of variables to hold values of any data type, and for their data type to be determined at runtime.   
This means that you do not need to explicitly declare the data type of a variable when you define it.  
Instead, the data type is inferred based on the value assigned to the variable.  
For example:
```python
x = 5       # x is an integer
x = "hello" # now x is a string
x = [1, 2, 3] # now x is a list
```
Here, x is initially assigned an integer value, then a string value, and finally a list value.  
Python adjusts the data type of x accordingly without requiring explicit type declarations.

Dynamic typing offers flexibility and simplicity, making Python code concise and easier to read and write.  
However, it also requires careful attention to variable types to avoid unexpected behavior.
 
**2. Can you explain the difference between static and dynamic typing, using Python as an example for dynamic typing?**
1. **Static Typing:**  
In statically-typed languages, such as C++, Java, or TypeScript, variables are required to be explicitly declared with their data types.  
Once a variable is declared with a certain data type, it cannot hold values of a different data type.  
Type checking typically occurs at compile-time, ensuring that only values of the declared type can be assigned to variables.    
Example in Java:
```java
int x = 5;       // x is an integer
x = "hello";     // Error: Type mismatch
```
2. **Dynamic Typing (Python):**  
In dynamically-typed languages, such as Python, variables are not required to be explicitly declared with their data types.  
Variables can hold values of any data type, and their data type is determined at runtime based on the value assigned to them.  
Type checking typically occurs at runtime, allowing for flexibility in variable assignments.  
Example in Python:
```python
x = 5       # x is an integer
x = "hello" # now x is a string
```
Key Differences:  
**Flexibility:** Dynamic typing offers greater flexibility because variables can change their data types during runtime, allowing for more dynamic programming.  
**Ease of Use:** Dynamic typing can make code shorter and easier to write, as you don't need to explicitly declare variable types.  
**Readability:** While dynamic typing can make code concise, it can also make it less readable if not used carefully, as the data type of a variable may not be immediately apparent from its declaration.  
**Type Safety:** Static typing provides better type safety because type checking occurs at compile-time, whereas in dynamic typing, errors related to incorrect types might only surface during runtime.  
  

**3. How Does Python Handle Different Data Types During Arithmetic Operations?**  
Python's approach to handling different data types during arithmetic operations depends on the specific data types involved.  
Here's a general overview:

**Numeric Types (int, float, complex):**  
Arithmetic operations involving numeric types are straightforward and follow the usual mathematical rules.  
Python automatically promotes operands to the most "complex" type involved in the operation to preserve precision.  
```python
x = 5 + 2.0    # x will be a float (7.0)
y = 3 * 4      # y will be an integer (12)
z = 2 + 3j     # z will be a complex number
```
**String Concatenation:**  
The + operator performs concatenation when applied to strings.  
Other arithmetic operations are not defined for strings.  
```python
s1 = "Hello "
s2 = "World"
s3 = s1 + s2   # s3 will be "Hello World"
```
**Mixed Types:**  
Python tries to coerce operands into compatible types for arithmetic operations.
```python
x = 5 + 2.0    # x will be a float (7.0)
y = "Hello " + str(5)   # y will be "Hello 5"
```
**Error Handling:**  
Python raises a TypeError if the operation is not defined for the given types.
```python
result = "Hello" / 2   # TypeError: unsupported operand type(s) for /: 'str' and 'int'
```
**Special Cases:**
Division (`/`) always returns a float, regardless of the types of the operands.  
Integer division (`//`) returns the floor division result, which is always an integer, even if the operands are floats.  
The % operator returns the remainder of division (modulo operation).  
Overall, Python is designed to handle different data types in a flexible manner, automatically promoting types as needed while still providing predictable behavior.  
However, it's essential to understand the specific behavior of each operation and the types involved to avoid unexpected results.

**4. Give an example of implicit type conversion in Python during an arithmetic operation.**
```python
x = 5     # x is an integer
y = 2.5   # y is a float

result = x + y

print(result)  # Output: 7.5
```
In this example, x is an integer (5) and y is a float (2.5).  
During the addition operation (x + y), Python implicitly converts the integer x to a float before performing the addition.  
This is because Python promotes operands to the most "complex" type involved in the operation to preserve precision.  
Therefore, x is converted to 5.0 before being added to y, resulting in the float 7.5.

**5. What will happen if you try to concatenate string with integer directly without type conversion?**  
If you try to concatenate a string with an integer directly without type conversion, Python will raise a `TypeError` because string concatenation is not defined for a string and an integer.  
Here's an example:
```python
s = "Hello"
n = 5

result = s + n  # Attempting to concatenate a string with an integer

# This line will raise a TypeError
print(result)
```
Attempting to run this code will result in a TypeError:

```python
TypeError: can only concatenate str (not "int") to str
```
To concatenate a string with an integer, you need to explicitly convert the integer to a string using the str() function:

```python
s = "Hello"
n = 5

result = s + str(n)  # Convert the integer to a string before concatenation

print(result)  # Output: Hello5
```
Now, n is converted to the string "5" before being concatenated with the string "Hello", resulting in the string "Hello5".

**6. What Happens When You Perform Integer Division with Zero in Python?**  
In Python, performing integer division by zero raises a `ZeroDivisionError`.  
This error occurs when you attempt to divide an integer by zero, which is mathematically undefined.  
```python
result = 5 // 0  # Attempting integer division by zero

# This line will raise a ZeroDivisionError
print(result)
```
Attempting to run this code will result in a ZeroDivisionError:
```
ZeroDivisionError: integer division or modulo by zero
```
Python does not allow division by zero in any form, whether it's integer division (`//`), floating-point division (`/`), or modulo operation (`%`).  
It's important to handle potential division by zero errors in your code to prevent unexpected crashes.  

**7. Explain the Use of the type() and isinstance() Functions.**  
In Python, the type() and isinstance() functions are commonly used for type checking and introspection.  
`type():`  
The `type()` function returns the type of an object.  
Syntax: `type(object)`
Example:
```python
x = 5
print(type(x))  # Output: <class 'int'>
```

`isinstance():`  
The `isinstance()` function checks if an object is an instance of a specified class or its subclasses.  
Syntax: `isinstance(object, classinfo)`
```python
x = 5
print(isinstance(x, int))  # Output: True
print(isinstance(x, float))  # Output: False
```
Use Cases:

**Type Checking:**
You can use `type()` to check the type of a single object.
You can use `isinstance()` to check if an object is an instance of a specific class or its subclasses, which is useful for checking inheritance relationships.  
**Conditional Execution:**  
isinstance() is often used within conditional statements to execute code based on the type of an object.  
**Loop Iteration:**  
isinstance() is also useful when iterating over a collection of objects and performing different actions based on their types.  
**Dynamic Behavior:**  
Both functions are commonly used in scenarios where the behavior of a program needs to adapt dynamically based on the types of objects being processed.  

Note:
While these functions can be helpful, it's often considered more Pythonic to rely on duck typing (i.e., behavior over explicit type) whenever possible.  
Overuse of type checking may indicate a design issue in the code and could lead to less flexible and more complex implementations.

## Coding Assignments
1. Simple Calculator:
    - Write a Python program that performs basic arithmetic operations (addition, subtraction, multiplication, division) on two user-input numbers. 
    - Handle different data types gracefully and provide appropriate output messages.
2. Temperature Converter:
    - Create a Python script that converts temperatures from Celsius to Fahrenheit and vice versa. 
    - Use float data types and ensure proper formatting of the output.

## Conclusion
- Today, we've learned about basic syntax, comments, and fundamental data types in Python.
- Practice these concepts to become familiar with Python's way of coding.
- In our next session, we'll cover variables, basic operators, and input/output in Python.
