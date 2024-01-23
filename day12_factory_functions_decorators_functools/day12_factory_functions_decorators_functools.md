# Decorators
- Decorators in Python are a powerful feature that allows you to modify the behavior of a function or class. 
- They are often used for adding functionality to existing code in a clean and maintainable manner. 

## Understanding Decorators
- In Python, functions are first-class objects, which means they can be passed around and used as arguments. 
- A decorator is a function that takes another function and extends its behavior without explicitly modifying it. 

### Robot Analogy
- Imagine you have a little robot named `say_hello`. 
- Its only job is to greet people. 
- So whenever you call `say_hello`, it simply says, "Hello!"

- Now, suppose you want your `say_hello` robot to do something extra, like say the time after greeting. 
- But you don't want to mess with its internal wiring or code. This is where a decorator comes in handy.

- Think of a decorator as a sort of robotic suit that you can wrap around your `say_hello` robot. 
- This suit enhances the robot's abilities without changing its core functionality of greeting.
- So, `my_decorator` is like this special suit. 
- You wrap your `say_hello` robot with this `my_decorator` suit and give it a new name, also say_hello (you could give it a different name, but here we're keeping the same name for simplicity).

Here’s what’s happening step-by-step:
1. You have your robot (`say_hello`): This robot can greet people by saying "Hello!".
2. You have a special suit (`my_decorator`): This suit can add new features to any robot it wraps. Let's say, for our example, it enables the robot to also tell the time after greeting.
3. You wrap your robot with the suit (`say_hello = my_decorator(say_hello)`): 
4. Now, when you activate your robot, it first says "Hello!" and then also tells the time.
4. Use your enhanced robot: Now every time you call say_hello, it does its original job (greeting) plus the extra job added by the decorator (saying the time).

In technical terms, 
- `say_hello` is a function, and `my_decorator` is another function that takes a function as input and returns a new function. 
- The new function is like the original `say_hello` function but with some added functionality.
- So, using a decorator is like giving your function a new suit that enhances its capabilities without changing the core of what it does.

Here’s a simple example:
```python
import time 
def my_decorator(func):
    def wrapper():
        func()
        print("Current time is:" + time.time())
    return wrapper

# Use the decorator
@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Hello!
# Current time is: 1706008954.2486143
```

##  Writing Your Own Decorators
- You can write your own decorators by defining a function that takes another function as an argument, defines a nested function inside, and returns that nested function. 
- Here's a more practical example, a decorator that times how long a function takes to execute:

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Executing {func.__name__} took {end_time - start_time} seconds.")
        return result
    return wrapper

@timer
def long_running_function():
    time.sleep(2)

long_running_function()
```


## Using @functools.wraps

### Robot analogy - with functools 
- So, you have your `say_hello` robot wrapped in the `my_decorator` suit, which enhances its functionality. 
- However, there's a small issue. 
- When you put a suit on a robot, it might become hard to remember what the original robot was like, especially if you have many robots with different suits. 
- You might want to ask, "Which robot is inside this suit?" or "What was the original purpose of this robot?"

- In Python, when you wrap a function with a decorator, the new function (the robot in the suit) can lose its identity. 
- It starts to look like the decorator function (the suit) rather than the original function (the robot). 
- This means you might lose important information like the original function's name, its documentation string (docstring), and other attributes.

- This is where `functools.wraps` comes into play. 
- Think of `functools.wraps` as a **special tag** you put on the suit that carries the name, documentation, and other details of the original robot. 
- Even though the robot is wearing a suit (decorator), anyone looking at it can tell exactly which robot is inside because of the tag.

Here's how it works in the context of our example:
- Original Robot (say_hello): This is your function that greets by saying "Hello!".
- Special Suit (my_decorator): This is your decorator that adds extra functionality, like telling the time after greeting. But it makes your robot look different from the outside.
- Using functools.wraps: Before you wrap your `say_hello` robot in the `my_decorator` suit, you attach a special tag (functools.wraps) to the suit. This tag carries the name, documentation, and other details of the say_hello robot.
- Wrap with the Tagged Suit: You put the suit on your robot. Now, even though your robot looks different because it's wearing the suit, anyone can read the tag (functools.wraps) and know that it's the say_hello robot inside.

First, without using `functools.wraps`, you will see that the metadata of the original function gets lost:
```python
import functools

def my_decorator(f):
    def wrapper(*args, **kwargs):
        print(f"Arguments were: {args}, {kwargs}")
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello(name):
    """Greet someone by their name."""
    print(f"Hello, {name}!")

say_hello("Alice")
print(say_hello.__name__)  # This will print 'wrapper'
print(say_hello.__doc__)   # This will print 'None'
```
Now, let's use functools.wraps within the decorator:

```python
import functools

def my_decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print(f"Arguments were: {args}, {kwargs}")
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello(name):
    """Greet someone by their name."""
    print(f"Hello, {name}!")

say_hello("Alice")
print(say_hello.__name__)  # This will correctly print 'say_hello'
print(say_hello.__doc__)   # This will correctly print 'Greet someone by their name.'
```
- By using functools.wraps, the say_hello function retains its metadata even after being decorated by my_decorator. 
- This is very important for introspection purposes and when you want your decorated functions to be properly documented and reflective of their original properties.

## Parameterized Decorators
- Sometimes you might want to pass extra arguments to your decorators. 
- For this, you need to create a **decorator factory** that returns a decorator.

```python
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")

# Hello Alice
# Hello Alice
# Hello Alice
```
- In this example, `repeat` is a **decorator factory** that takes an argument and **returns a decorator**. 
- The **returned decorator then takes a function and returns the wrapper function**.

## Stacking Decorators
- Python allows you to stack multiple decorators. 
- When stacking decorators, the order matters. 
- Here's an example:
```python
@decorator2
@decorator1
def func():
    pass
```
This is equivalent to:
```python
func = decorator2(decorator1(func))
```

Here's a practical example with actual decorators:
```python
import time
def say_time(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(time.time())
    return wrapper


def say_args(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(f"{args} {kwargs}")
    return wrapper

@say_time
@say_args
def greet(name):
    print(f"hello {name}")


greet("ranjan")
# greet = say_time(say_args(greet))

# output:
# hello ranjan
# ('ranjan',) {}
# 1706006791.417261

```
- In your code, you have defined two decorators `say_time` and `say_args`, and applied them to the greet function. 
- When you call greet("ranjan"), the flow of execution is as follows:

1. `say_args` is the outermost decorator, so its wrapper function is called first.
2. Inside `say_args.wrapper`, `func(*args, **kwargs)` calls the next function in the chain, which is `say_time.wrapper` because say_time is the next decorator.
3. `say_time.wrapper` calls its func(*args, **kwargs), which is the original `greet` function.
4. The original greet function executes and prints "hello ranjan".
5. After the greet function finishes, control goes back to say_time.wrapper, which then prints the current time.
6. Then control goes back to say_args.wrapper, which prints the arguments and keyword arguments.
