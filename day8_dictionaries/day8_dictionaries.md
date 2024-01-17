## What is a Dictionary?
- A dictionary in Python is a **collection of key-value pairs**. 
- Each key-value pair maps the key to its associated value.
```python
{
    "id": 1,
    "name": "Soumya Ranjan",
    "phone": "123456",
    "website": "whatever.org"
  }
```
## What is a Key-Value Pair?
- A key-value pair in a dictionary is a set of two linked data items:
- **Key:** A unique identifier where you can find your data (similar to a name).
- **Value:** The data that you want to store or retrieve (similar to a definition).

## Order and Mutability in Dictionaries
### Order:
**Before Python 3.7:** 
- Dictionaries were **unordered**. 
- The order of items did not necessarily reflect the order of item insertion, and iterating over a dictionary's elements could return them in any order.

**Python 3.7 and later:** 
- Dictionaries are **ordered**. 
- As of Python 3.7, the dictionary maintains the insertion order, meaning items are returned in the order they were added. 
- This was an implementation detail in Python 3.6 (in the CPython implementation) and was made an official part of the Python language specification in Python 3.7.
```python
{
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org"
  }
```
- The order of the keys in `my_dict` will be exactly the same as the order in which they were defined in the dictionary literal. 
- In this case, "id" will be the first key, "name" the second, "username" the third, and so on.


### Mutability:
- **Dictionaries are mutable**. 
- You can add, remove, or modify items after the dictionary's creation. 
- The keys of a dictionary, however, must be of immutable types (like strings, numbers, or tuples containing only immutable elements). 
- This is because dictionaries use these keys to compute and store the item's position in the memory, and this position should not change over time.

## Basic Dictionary Operations
### Creating Dictionaries
There are various ways to create dictionaries in Python.
1. **Using Curly Braces {}**
- You can create a dictionary by enclosing key-value pairs in curly braces {}. 
- Keys and values are separated by a colon `:`
```python
# Creating a dictionary with integer keys
dict1 = {1: 'apple', 2: 'banana'}

# Creating a dictionary with mixed key types
dict2 = {'name': 'John', 1: [2, 4, 3]}
```
2. **Using the dict() Constructor**
- You can also use the `dict()` constructor to create dictionaries.
```python
# Using dict() without any parameters
dict3 = dict()

# Using dict() with key-value pairs
dict4 = dict({1: 'apple', 2: 'banana'})

# Creating a dictionary from a list of tuples
dict5 = dict([(1, 'apple'), (2, 'banana')])
```
3. **Using zip():**

- Combining two lists or iterables into key-value pairs.
```python
keys = ['name', 'age']
values = ['John', 25]
my_dict = dict(zip(keys, values))
# Output: {'name': 'John', 'age': 25}
```
### Accessing Elements
- You can access elements in a dictionary by using their keys.
```python
# Accessing an element using a key
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Accessing element
print(my_dict['b'])
# Updating element
my_dict['c'] = 30 
# Adding new element
my_dict['d'] = 4

print(my_dict)
```


## Common Dictionary Methods
1. ### `dict.get(key, default=None)`
- The `get()` method in Python is used to **retrieve the value of a specified key** from a dictionary. 
- It's a safer alternative to the standard way of accessing dictionary values by key because it allows you to handle cases where the key might not be present in the dictionary without raising an error.
- **Syntax:** `dict.get(key, default=None)`
  - key: The key for which you want to retrieve the value.
  - default (optional): The value to return if the specified key is not found. The default value is None if this parameter is not specified.
- **Behavior:**
  - If the key is in the dictionary, get() returns the value for that key.
  - If the key is not found and the default parameter is specified, it returns the value of default.
  - If the key is not found and the default parameter is not specified, it returns None.
- **Advantages of using get():**
  - It provides a way to access dictionary values without risking a KeyError.
  - It allows you to easily provide a default value if the key is not found.
  - It makes your code safer and more readable, especially when dealing with user-generated or unpredictable data.
  - `get()` is especially useful in scenarios where you're not sure if a key exists and you want to avoid exceptions disrupting the flow of your program. 
  - It's a common practice to use get() when dealing with dictionaries in Python.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Key is present
print(my_dict.get('a'))  # Output: 1

# Key is not present, default is not provided
print(my_dict.get('d'))  # Output: None

# Key is not present, default is provided
print(my_dict.get('d', 'Not Found'))  # Output: 'Not Found'
```


2. ### `dict.setdefault(key, default=None)`
- The `setdefault()` method in Python is used with dictionaries to retrieve the value of a specified key, similar to the get() method. 
- However, setdefault() has an additional functionality: **if the key does not exist in the dictionary, it inserts the key with a specified default value.**
- **Syntax**: `dict.setdefault(key, default=None)`
  - key: The key for which you want to retrieve the value.
  - default_value (optional): 
    - The value to set and return if the specified key is not found. 
    - If this parameter is not specified and the key is not found, the default value is None.
- **Behavior**:
  - If the key is in the dictionary, setdefault() returns the value for that key.
  - If the key is not found:
    - It inserts the key with the default_value.
    - If default_value is specified, it returns default_value.
    - If default_value is not specified, it returns None.
- **Advantages of using setdefault():**
  - It can be used to initialize dictionary keys with a default value when keys are being added dynamically.
  - setdefault() is a method that combines the functionality of checking for a key and possibly inserting a new key with a default value if the key does not exist. 
  - It's particularly useful when you are building dictionaries on-the-fly and want to ensure that keys are initialized to a default value the first time you see them.

```python
my_dict = {'a': 1, 'b': 2}

# Key is present
print(my_dict.setdefault('a', 'Not Found'))  # Output: 1
print(my_dict)  # Output: {'a': 1, 'b': 2}

# Key is not present, default is not provided
print(my_dict.setdefault('c'))  # Output: None
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': None}

# Key is not present, default is provided
print(my_dict.setdefault('d', 4))  # Output: 4
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': None, 'd': 4}
```

3. ### `dict.keys()`
- The `keys()` method in Python is used with dictionaries to get a view object that displays a list of all the keys in the dictionary. 
- The keys() method is commonly used when you want to iterate over the keys of a dictionary or when you need to check if a particular key exists in the dictionary.
- It's a way to access, iterate over, or check for the presence of keys in a dictionary.
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

keys = my_dict.keys()
print(keys)  # Output: dict_keys(['a', 'b', 'c'])

# Iterating over keys
for key in keys:
    print(key)
# Output:
# a
# b
# c

# Checking if a key is present
if 'a' in keys:
    print("'a' is a key in the dictionary")
# Output: 'a' is a key in the dictionary
```

4. ### `dict.values()`
- The `values()` method in Python is used with dictionaries to get a view object that displays a list of all the values in the dictionary. 
- The `values()` method is commonly used when you want to iterate over the keys of a dictionary or when you need to check if a particular value exists in the dictionary.
- It's a way to access, iterate over, or check for the presence of values in a dictionary.
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

values = my_dict.values()
print(values)  # Output: dict_values([1, 2, 3])

# Iterating over values
for value in values:
    print(value)
# Output:
# 1
# 2
# 3

# Checking if a value is present
if 1 in values:
    print("1 is a value in the dictionary")
# Output: 1 is a value in the dictionary
```

5. ### `dict.items()`
- The `items()` method in Python is used with dictionaries to get a view object that displays a list of the dictionary's key-value pairs as tuples. 
- - The `items()` method is widely used when you need to work with both keys and values of a dictionary. 
- It's particularly useful in loops where you want to access both the key and the value at the same time. 

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

items = my_dict.items()
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Iterating over key-value pairs
for key, value in items:
    print(f"{key}: {value}")
# Output:
# a: 1
# b: 2
# c: 3

# Checking if a key-value pair is present
if ('a', 1) in items:
    print("The key-value pair ('a', 1) is in the dictionary")
# Output: The key-value pair ('a', 1) is in the dictionary
```
6. ### `dict.update([other])`
- The `update()` method in Python is used with dictionaries to add key-value pairs from another dictionary or an iterable of key-value pairs to the current dictionary. 
- It modifies the dictionary in place, meaning the changes are made directly to the original dictionary.
- **Syntax:** `dict.update([other])`
  - other can be a dictionary or an iterable of key-value pairs (e.g., tuples).
- **Behavior:**
  - Adds key-value pairs from other to the dictionary.
  - Updates the value of a key if it already exists in the dictionary.
  - Adds a new key-value pair to the dictionary if the key does not exist.

**Updating with another dictionary:**
Here, the value of 'b' is updated to 3, and the key-value pair 'c': 4 is added.
```python
my_dict = {'a': 1, 'b': 2}
other_dict = {'b': 3, 'c': 4}

my_dict.update(other_dict)
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
```
**Updating with an iterable of key-value pairs:**
```python
my_dict = {'a': 1, 'b': 2}
pairs = [('b', 3), ('c', 4)]

my_dict.update(pairs)
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
```
**Using keyword arguments:**
You can also use keyword arguments to update the dictionary.
```python
my_dict = {'a': 1, 'b': 2}
my_dict.update(b=3, c=4)
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
```

7. ### `pop(key[, default])`
- This method removes the item with the specified key and returns its value.
- If the key is found, it removes the key-value pair from the dictionary and returns the value.
- If the key is not found and the default value is specified, it returns the default value.
- If the key is not found and no default value is specified, it raises a KeyError.
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Use case 1: Key is found, removes the key-value pair and returns the value
value_case_1 = my_dict.pop('b')
print("Use Case 1:")
print(f"Value removed: {value_case_1}")  # 2
print(f"Updated dictionary: {my_dict}")  # {'a': 1, 'c': 3}

# Use case 2: Key is not found, returns the default value
default_value = -1  # Default value to return if 'x' is not found
value_case_2 = my_dict.pop('x', default_value)
print("\nUse Case 2:")
print(f"Value removed or default: {value_case_2}")  # -1
print(f"Updated dictionary: {my_dict}")  # {'a': 1, 'c': 3}

# Use case 3: Key is not found, no default value specified, raises KeyError
try:
    value_case_3 = my_dict.pop('y')
except KeyError as e:
    print("\nUse Case 3:")
    print(f"Key 'y' not found, raising KeyError: {e}")  # Key 'y' not found, raising KeyError: 'y'
```

9. ### `popitem():`
- This method removes and returns the last inserted key-value pair 
- In dictionaries before Python 3.7, it removes and returns a random item because dictionaries were unordered
- If the dictionary is empty, calling popitem() causes a KeyError.
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
item = my_dict.popitem()  # Removes and returns the last inserted item, e.g., ('c', 3)
print(my_dict)  # Output might be: {'a': 1, 'b': 2}
print(item)  # Output: ('c', 3)
```

10. ### `del()`
- The `del` statement in Python is used to delete items from a dictionary. 
- It allows you to remove an item from a dictionary by key. 
- Here's how you use del with dictionaries: `del dict[key]`
- Behavior: This statement removes the key-value pair from the dictionary where the key matches the specified key.
  - If the key is found, it will remove the key-value pair.
  - If the key is not in the dictionary, it will raise a KeyError.
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']  # Removes the key-value pair where key is 'b'
print(my_dict)  # Output: {'a': 1, 'c': 3}

del my_dict['z']  # KeyError: 'z'
```
**Deleting Entire Dictionary:**
- You can also use del to delete the entire dictionary. 
- After deletion, the dictionary no longer exists, and trying to access it will raise a NameError.
```python
del my_dict  # Deletes the entire dictionary
print(my_dict)  # This will raise NameError as my_dict no longer exists
```
**Differences from pop and popitem:**
- Unlike `pop` and `popitem`, `del` does not return the value of the removed item. It simply deletes the item.
- del can also be used to delete the entire dictionary, not just individual items.

11. ### `dict.clear()`
- Removes all the elements from the dictionary.
```python
my_dict = {'name': 'Alice', 'age': 25}
my_dict.clear()
print(my_dict)  # Output: {}
```

## Nested Dictionaries
### Sample Data
```python
nested_dict = {
    'key1': {
        'key2': 'value1',
        'key3': {
            'key4': 'value2',
            'key5': 'value3'
        }
    },
    'key6': {
        'key7': 'value4'
    }
}
```
- In this structure:
  - key1 and key6 are the outer keys.
  - key1 contains another dictionary with keys key2 and key3.
  - key3 itself contains another dictionary.

### Accessing Data:

**Direct Access:**
```python
# Accessing 'value1' using direct chaining of keys
inner_value = nested_dict['key1']['key2']  # inner_value will be 'value1'
```
**Using .get() method:**
```python
# Safely accessing 'value3' using .get(), defaulting to 'Not Found' if any key is missing
inner_value = nested_dict.get('key1').get('key3').get('key5')  # inner_value will be 'value3'
```

### Modifying Data:

**Changing Values:**
```python
# Changing the value associated with 'key2' under 'key1'
nested_dict['key1']['key2'] = 'new_value1'  # 'value1' is now changed to 'new_value1'
```
**Adding New Key-Value Pairs:**
```python
# Adding a new key-value pair under 'key3'
nested_dict['key1']['key3']['new_key'] = 'new_value2'  # Adds 'new_key': 'new_value2' under 'key3'
```

### Iterating through the nested dictionary
```python
for outer_key, nested_dict in nested_dict.items():
    for inner_key, value in nested_dict.items():
        # Process the value or keys here
        print(f"Outer Key: {outer_key}, Inner Key: {inner_key}, Value: {value}")
```
---
---

### Assignments
1. **Dictionary Creation:**
- Write Python code to create an empty dictionary called `student_scores`. 
- Then, add three students and their corresponding scores to the dictionary. 
- Print out the dictionary at the end.

2. **Dictionary Access:**
- Given the following dictionary of student grades:
- `student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}`
- Write code to retrieve the highest grade and print corresponding name

3. **Dictionary Iteration:**
- Given the dictionary colors:
- `colors = {'apple':'red', 'banana':'yellow', 'grape':'purple', 'cherry':'red', 'guava':'yellow'}`
- Write a loop that iterates through the dictionary and prints the name of fruits grouped by color. See output below.
```python
red: appple, cherry
yellow: banana, guava
purple: grape
```

4. **Character Frequency Counter:**
- Write a program that takes a string as input and uses a dictionary to count the frequency of each character in the string. 
- Print out the character frequencies as key-value pairs.

5. **Phonebook:**
- Implement a simple phonebook using a dictionary. 
- Initially, create an empty dictionary called phonebook. 
- Then, allow the user to add new contacts, update existing contacts, and search for a contact by name.
---
### Interview Questions
1. Explain the computational complexity (time complexity) of common dictionary operations, such as inserting a key-value pair, retrieving a value by key, and checking for the existence of a key.
2. Discuss the differences between hash tables and dictionaries in Python. How does Python's dictionary implementation work internally to provide fast access to key-value pairs?
3. What is a hash function, and why is it important in the context of dictionaries?
4. Python 3.7 introduced dictionary ordering. Describe how dictionary ordering affects the behavior of dictionaries, especially in terms of iteration and maintenance of key-value pairs' order.
