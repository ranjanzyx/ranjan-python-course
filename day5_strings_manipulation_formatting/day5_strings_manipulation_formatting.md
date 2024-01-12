# Strings in Python

### 1. Definition
- A string in Python is essentially a sequence of characters. 
- Anything enclosed in single (`'...'`) or double quotes (`"..."`) is considered a string. 
- This can include alphabets, digits, symbols, and even spaces. 
```python
# Creating strings
string_with_single_quotes = 'Hello, World!'
string_with_double_quotes = "Python is fun!"

# Printing strings
print(string_with_single_quotes)
print(string_with_double_quotes)
```

### 2. Immutability
- Once a string is created, its contents cannot be altered. This is referred to as immutability. 
- You cannot change, add, or remove characters directly in the existing string. 
- However, you can create new strings based on modifications of the old one. 
```python
original_string = "Python"
print("Original String:", original_string)
print("ID of Original String:", id(original_string))  # 1933745763760

# Attempting to modify the original string (this would raise an error if uncommented)
# original_string[0] = "J"

# This line creates a new string by concatenating 'J' with 'original_string'
original_string = "J" + original_string
# This demonstrates the immutability of strings in Python - we're not modifying the original string, but creating a new one.
print("ID of Original String:", id(original_string))  # 1933746165808
```

### 3. Indexing
- Each character in a string can be accessed using its index. 
- Indexing starts from 0. 
- So, in the string '**Python**', the character 'P' is at index 0, 'y' is at index 1, and so on. 
- Python also supports negative indexing where -1 refers to the last character, -2 to the second last, and so on.
```python
my_string = "Python"

# Accessing characters using positive indexing
first_char = my_string[0]  # 'P'
second_char = my_string[1]  # 'y'

# Accessing characters using negative indexing
last_char = my_string[-1]  # 'n'
second_last_char = my_string[-2]  # 'o'

# Printing characters
print(f"First character: {first_char}, Second character: {second_char}")
print(f"Last character: {last_char}, Second last character: {second_last_char}")
```

## String Functions
1. **.len()** Determines the length of a string.
2. **.replace(old, new):** Replaces occurrences of a substring within the string.
4. **.split(separator):** Splits a string into a list of substrings based on a separator.
5. **.join(iterable):** Joins elements of an iterable (like a list) into a single string with the string acting as a separator.
5. **.strip():** Removes whitespace from the beginning and end of a string.
6. **.find(substring):** Returns the lowest index of the substring if found, else returns -1.
7. **.upper() / .lower():** Converts all characters in a string to upper case or lower case.
8. **startswith / endswith:** Checks if a string starts or ends with a specified substring.
9. **index / rindex:** Finds the position of a substring within a string.

```python
# String to work with
text = "Hello World"

# len
print(len(text))  # 11

# replace
print(text.replace('World', 'Everyone'))  # Hello Everyone

# split (by space)
print(text.split(" "))  # ['Hello', 'World']

# join
words = ["Hello", "world", "Python"]
print(",".join(words))  # Hello,world,Python

# strip
trimmed_text = "   Hello World   "
print(trimmed_text.strip())  # Hello World

# find
substring = "World"
print(text.find(substring))  # 6

# upper and lower
print(text.upper())  # HELLO WORLD
print(text.lower())  # hello world

# startswith / endswith
print(text.startswith("Hello"))  # True
print(text.endswith("World"))  # True

# index / rindex
print(text.index('o'))  # 4
print(text.rindex('o'))  # 7
```

### String Slicing
- In Python, "slicing" is a technique used to extract a part of a sequence such as a list, tuple, or string. 
- It's done by specifying a range of indices in square brackets, typically using the format **[start:stop:step]**, where:
  - **start** is the index where the slice starts (inclusive).
  - **stop** is the index where the slice ends (exclusive).
  - **step** is the amount by which the index increases.
- If step is omitted, it defaults to 1. 
- If start or stop is omitted, slicing will start from the beginning or continue to the end, respectively.
```python
my_string = "Hello, world!"
print(my_string[:5])  # Output: Hello
print(my_string[7:])  # Output: world!
print(my_string[0:6:2]) # Output: Hlo
```

### String Formatting
- String formatting in Python is a powerful way to construct and format strings dynamically. 
- There are several methods to perform string formatting in Python:

#### 1. % Operator (Old Style)
- This is an older method for formatting strings. 
- It uses the `%` operator and is similar to printf-style string formatting in C.
```
name = "John"
age = 30
formatted_string = "Hello, %s. You are %d years old." % (name, age)
print(formatted_string)  # Hello, John. You are 30 years old.
```

#### 2. str.format() Method (New Style)
- Introduced in Python 2.6, this method is more powerful and flexible. 
- It uses curly braces {} as placeholders.

```python
name = "Alice"
age = 25
formatted_string = "Hello, {}. You are {} years old.".format(name, age)
print(formatted_string)  # Hello, Alice. You are 25 years old.

# With positional and keyword arguments
formatted_string = "Hello, {0}. You are {1} years old. Nice to meet you, {0}.".format(name, age)
print(formatted_string)  # Hello, Alice. You are 25 years old. Nice to meet you, Alice.
```

#### 3. F-Strings (Literal String Interpolation)
- Introduced in Python 3.6, f-strings are a concise and readable way to embed expressions inside string literals, using curly braces {}.

```python
name = "Bob"
age = 28
formatted_string = f"Hello, {name}. You are {age} years old."
print(formatted_string)  # Hello, Bob. You are 28 years old.

# With expressions
formatted_string = f"{name} will be {age + 2} years old in two years."
print(formatted_string)  # Bob will be 30 years old in two years.
```
#### Formatting Options
```python
# Formatting decimal places
number = 123.4567
formatted_string = f"Formatted number: {number:.2f}"  # Formatted number: 123.46
print(formatted_string)

# Padding and Alignment
# Right alignment with padding
formatted_string = f"|{'right':>10}|"
print(formatted_string)  # |     right|

# Left alignment with padding
formatted_string = f"|{'left':<10}|"
print(formatted_string)  # |left      |

# Center alignment with padding
formatted_string = f"|{'center':^10}|"
print(formatted_string)  # |  center  |
```

### String Comparision
```python
# Equality (==): Checks if two strings are exactly the same in terms of their content. It is case-sensitive.
"Hello" == "hello"  # False, because of different case
"Python" == "Python"  # True, because they are exactly the same

# Inequality (!=): Checks if two strings are not the same.
"Apple" != "Orange"  # True, because they are different

# Greater than (>), Less than (<), Greater than or equal to (>=), Less than or equal to (<=): 
# These comparisons are based on the lexicographical order (similar to alphabetical order, but based on ASCII values for each character).
"apple" < "banana"  # True, because 'apple' comes before 'banana' lexicographically
"apple" > "Apple"   # True, because lowercase letters have higher ASCII values than uppercase
"cat" >= "cat"      # True, because they are exactly the same

# Case Insensitive Comparisons: To perform case-insensitive comparisons, you can convert both strings to the same case (either upper or lower) before comparison.
"Hello".lower() == "hello".lower()  # True, after converting both to lowercase
"Python".upper() == "PYTHON".upper()  # True, after converting both to uppercase

# String Methods for Comparison: Python also provides string methods like startswith(), endswith(), and in operator for substring checks.
"Hello World".startswith("Hello")  # True
"Hello World".endswith("World")    # True
"ell" in "Hello"                   # True
```
### Raw Strings
- A raw string in Python is a string prefixed with an **'r'** or **'R'**. 
- It treats backslashes (\\) as literal characters and does not interpret them as escape characters. 
- This is particularly useful when dealing with strings that contain many backslashes, such as file paths or regular expressions.

```python
# A normal string with escape sequences
normal_string = "This is a \n new line."
print(normal_string)
# This is a 
#  new line.

# A raw string ignores escape sequences like \n
# Output will be in a single line with \n as part of the string
raw_string = r"This is a \n new line."
print(raw_string)  # This is a \n new line.
```
