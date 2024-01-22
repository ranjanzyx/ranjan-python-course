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