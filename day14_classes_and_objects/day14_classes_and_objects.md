##  Introduction to Object-Oriented Programming (OOP)
- Imagine you're a chef in a kitchen. 
- In this kitchen, you have different types of utensils and ingredients. 
- Each type of utensil (like a frying pan or a spatula) has specific uses and ways to be handled, and each ingredient (like an onion or tomato) has its characteristics and ways it can be used. 
- Object-Oriented Programming (OOP) is somewhat like this kitchen.

- In OOP, everything is seen as an "object" – similar to how each utensil and ingredient in the kitchen is a distinct item with its specific features and uses.

## Key OOP Principles
1. **Encapsulation:** Understand how to bundle the data and the methods that operate on the data within one unit.
2. **Abstraction:** Learn to hide complex implementation details and show only the necessary features of an object.
3. **Inheritance:** Understand how a class can inherit attributes and methods from another class.
4. **Polymorphism:** Learn how to use a unified interface to operate on objects of different classes.

Let's continue with our kitchen analogy to understand the four key principles of Object-Oriented Programming (OOP): Encapsulation, Abstraction, Inheritance, and Polymorphism.

### Encapsulation
- Think of encapsulation as using a multi-compartment lunchbox to carry your meal. 
- Each compartment represents a section of the class where you store related items (data and methods). 
- For example, one compartment might hold a sandwich (data), and the lid (methods) might have instructions on how to eat it without making a mess. 
- Encapsulation allows you to:
  - **Bundle Data and Methods:** Just like a lunchbox holds both your food and the utensils to eat it, in encapsulation, data and the methods to manipulate the data are bundled together.
  - **Restrict Access:** You don't want everything in your lunchbox to be accessible to everyone. Similarly, encapsulation restricts direct access to some of the object's components, which can prevent accidental or unauthorized interactions.
### Abstraction
- Abstraction in OOP is like using a modern kitchen appliance, like a microwave. 
- You don't need to know all the complex engineering and physics behind how it works. 
- You only need to know the interface – the buttons and settings to use it. 
- Abstraction in OOP allows you to:
  - **Hide Complex Details:** Just like you don't need to know the microwave's inner workings, abstraction lets you hide the complex implementation details of a class from the user.
  - **Show Only the Necessary:** The microwave only shows what you need to know (buttons and settings). Similarly, abstraction lets you expose only the necessary methods and properties of an object, making the interface simpler and easier to use.
### Inheritance
- Imagine you have a basic recipe for a salad, and you want to make a variation of it, like a Greek salad. 
- Instead of writing a new recipe from scratch, you take the basic salad recipe and add some ingredients or steps to it. 
- This is inheritance – creating a new class (Greek salad) based on an existing class (basic salad) while retaining its features and adding new ones.
- Inheritance allows you to:
  - **Inherit Attributes and Methods:** A child class inherits all the attributes (ingredients) and methods (cooking steps) from the parent class but can also have its own unique attributes and methods.
  - **Avoid Code Duplication:** Just like you don't rewrite the entire salad recipe every time, inheritance lets you reuse code from parent classes, reducing redundancy and making the codebase cleaner and easier to maintain.
### Polymorphism
- This is like having different types of knives for cutting. 
- Each knife (object) can be used for cutting (method), but the way it cuts (behavior) can be different. 
- A serrated knife saws through bread, and a chef's knife chops vegetables. 
- They perform the same function (cutting), but the way they do it is different, depending on the object.
- Polymorphism allows you to:
  - **Use a Unified Interface:** Just like the action 'cut' can be applied to any knife, polymorphism lets you use a single interface (method name) to operate on objects of different classes.
  - **Implement Methods Differently:** Each knife cuts differently. Similarly, different classes can have their own implementation of the same interface or method. This is useful when different objects need to perform the same action in different ways.
By understanding and implementing these four pillars of OOP – Encapsulation, Abstraction, Inheritance, and Polymorphism – you can create a well-structured, efficient, and scalable codebase, much like running an efficient, versatile, and organized kitchen!

## Advantages of OOP
### 1. Code Reusability:
- Just like once you create a recipe, you can use it to make that dish as many times as you want, in OOP, once a class is written, it can be used to create multiple objects. 
- This avoids repetition and makes code easier to maintain.

### 2. Scalability:
- Imagine your kitchen can easily add new appliances or ingredients. 
- Similarly, OOP makes it easy to add new features and elements to your software. 
- You can create new classes or extend existing ones without drastically altering the existing code.

### 3. Manageability:
- A well-organized kitchen allows you to work more efficiently, knowing exactly where each utensil and ingredient is. 
- OOP allows you to organize your code into classes and objects, making it easier to manage, especially in large software projects where managing code can get complicated.

In summary, OOP is like running a kitchen, where: 
- utensils and ingredients are objects, 
- recipes are classes, and 
- the principles of OOP help in making the kitchen (software) more efficient, easier to manage, and scalable.

# OOPS and Python:
- Let's continue with the kitchen analogy to explain `classes` and `objects` in Python, along with some core concepts like the `__init__` method, instance variables, and methods.

## Defining Classes
- Think of a class as a recipe. 
- It's a blueprint for how to make something. 
- In this case, let's say we're making a recipe for a cake. 
- The recipe outlines what ingredients you need and the steps to make it, but it's not the cake itself.

```python
class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

    def describe(self):
        print(f"This is a {self.flavor} cake.")
```
In this code:
- `class Cake`: starts the definition of our class (recipe).
- The `__init__` method is called automatically every time the class is being used to create a new object. This method sets up the object.
- `self.flavor = flavor` initializes the flavor of the cake. `self` represents the instance (specific cake) of the class (recipe), and `flavor` is an attribute.

## Creating Objects
- If the class is like a recipe, then an object is like the actual cake you bake using that recipe. 
- It's a real, tangible thing you can see and eat.

```python
my_cake = Cake("chocolate")
```
In this code:
`my_cake` is an instance (object) of the `Cake` class. You've made a chocolate cake!


## The `__init__` Method
- The `__init__` method is like the part of the recipe that tells you what ingredients to prepare before you start following the steps of the recipe. 
- It sets up your cake (object) with everything it needs to be a cake.

In the Cake class example:
- `__init__(self, flavor)` is preparing your cake by setting its flavor.

## Instance Variables and Methods
- Instance variables are like the specific ingredients for your cake. 
- If your recipe (class) says you need flour, each cake (object) you make might use a different amount of flour. 
- The flour for each cake is like an instance variable.

- Instance methods are like the steps in your recipe. 
- They tell you what you can do with your cake. 
- Maybe your recipe has a step to frost the cake. That's like an instance method.

In the Cake class example:
- `self.flavor = flavor` is an instance variable. Each cake can have a different flavor.
- `describe(self)` is an instance method. It allows the cake to describe itself.

When you put all these together in Python:

```python
class Cake:
    def __init__(self, flavor):
        self.flavor = flavor  # Instance variable

    def describe(self):  # Instance method
        print(f"This is a {self.flavor} cake.")

# Creating a Cake object
my_cake = Cake("chocolate")

# Using an instance method
my_cake.describe()  # Output: This is a chocolate cake.
```

- So, when you're using classes and objects in Python, think of it as writing and following a recipe in a kitchen.
- You have your recipe (class), your ingredients (instance variables), and your cooking steps (instance methods).
- And just like in cooking, you can create many different cakes (objects) from the same recipe (class), each with its own specific flavors and decorations (attributes and methods).

## Introduction to Class Variables and Class Methods
- In object-oriented programming, especially in Python, classes act as blueprints for creating objects. 
- Classes can contain two main types of components: **variables** and **methods**. 
- Among these, there are distinctions based on whether they belong to the class itself or to instances of the class. 
- This brings us to class variables and class methods.

### Introduction to Class Variables
- Class variables are variables that are shared across all instances of a class. 
- They hold the same value for every instance of the class, making them ideal for storing properties that are common to all objects of the class. 
- If the value of a class variable is changed, the change is reflected across all instances.

### Introduction to Class Methods
- Class methods are methods that are bound to the class rather than its instances. 
- They can access and modify class state (i.e., class variables) that applies across all instances of the class. 
- Class methods are not concerned with individual instance variables. 
- Instead, they operate at the class level, affecting all instances of the class.

Let's consider the Cake class:

```python
class Cake:
    shape = "round"  # Class variable: Shared among all cakes

    def __init__(self, flavor):
        self.flavor = flavor  # Instance variable: Unique to each cake

    @classmethod
    def set_shape(cls, new_shape):
        cls.shape = new_shape  # Class method: Updates the shape for all cakes
```
In this class:
- **shape** is a `class variable`, meaning every Cake instance will initially have a shape of "round".
- **flavor** is an `instance variable`, meaning each Cake instance can have a different flavor.
- **set_shape** is a `class method` used to change the shape class variable, affecting the shape of all cakes, not just an individual cake.

### Explanation of `@classmethod`, `cls`, and Alternative Names
- `@classmethod` is a decorator in Python, indicating the following method is a class method.
- `cls` is a conventional parameter name in class methods, referring to the class itself. 
- While cls is not a keyword and you could technically use another name, it's a strong convention in Python to use `cls` for class methods, just like self is used for instance methods to refer to the instance.

### What Happens If We Don't Use @classmethod
- If you don't use the `@classmethod` decorator, the method will not be treated as a class method. 
- Instead, it will be considered an instance method and will expect self as the first parameter, referring to the instance of the class, not the class itself. 
- This means it won't be able to modify class variables in the way class methods can unless accessed through the class name explicitly.

### Expanding on the Cake Class Example
**Using set_shape with Object and Class References**
  - **Object Reference:** 
    - Even though `set_shape` is a class method (affecting the class variable for all instances), you can still call it on an instance of the class. 
    - For example: `chocolate_cake.set_shape("square")`
    - This will change the shape for all instances of `Cake`, not just for `chocolate_cake`. 
    - It's the same as calling `Cake.set_shape("square")`.

  - **Class Reference:** 
    - The typical way to use a class method is on the class itself, not on an instance of the class. 
    - For example: `Cake.set_shape("square")`
    - This makes it clear that the method is intended to operate on the class level, affecting all instances of the class.

### Objects Created Before and After Modifying Class Variables
- **Before Modification:** 
    - Objects created before the modification of a class variable retain access to the class variable. 
    - However, if the class variable is modified, these objects will see the new value, as class variables are shared across all instances.
```python
chocolate_cake = Cake("chocolate")  # shape is initially "round"
Cake.set_shape("square")  # shape changed to "square"
print(chocolate_cake.shape)  # This will print "square"
```
- **After Modification:** 
  - Objects created after the modification of a class variable will inherently access the modified class variable.
```python
Cake.set_shape("square")  # shape changed to "square"
vanilla_cake = Cake("vanilla")  # shape is "square" for this new object
```

## Static Methods
- Static methods, much like class methods, are a way to encapsulate functionality in a class without requiring a reference to a particular instance or the class itself. 
- They are marked with the `@staticmethod` decorator, indicating that they do not automatically receive an instance (`self`) or class (`cls`) reference as their first argument. 

### Introduction to Static Methods
- Static methods are functions defined within a class that don't access or modify the class state (class variables) or instance state (instance variables). 
- They are **utility functions that perform a task in isolation**.

- **Definition:** Static methods are defined using the `@staticmethod` decorator.
- **No self or cls:** Unlike instance methods or class methods, static methods do not receive an implicit first argument, either self or cls.
- **Utility Functions:** They are often used to implement functionality that logically belongs to the class but does not need to access the class or instance-specific data.


- Let's say we want to add a functionality to the Cake class that can suggest a serving size based on the cake's size, 
  but this calculation does not depend on the specific cake instance's properties nor the class's properties. 
- This is a perfect scenario for a static method.

```python
class Cake:
    shape = "round"  # Class variable: Shared among all cakes

    def __init__(self, flavor):
        self.flavor = flavor  # Instance variable: Unique to each cake

    @classmethod
    def set_shape(cls, new_shape):
        cls.shape = new_shape  # Class method: Updates the shape for all cakes

    @staticmethod
    def serving_size(cake_size):
        if cake_size <= 6:
            return "Small - Serves 2-4"
        elif cake_size <= 10:
            return "Medium - Serves 5-8"
        else:
            return "Large - Serves 9+"
```
In this class:

- `serving_size` is a **static method**, meaning it can be called on the class itself, not on a specific instance, and it doesn't modify the class or instance state.
- `cake_size` is just a regular parameter you pass to the method. It doesn't have any special behavior like `self` or `cls`.

### Usage of Static Methods
- You can call a static method using the class name, similar to class methods:
```python
print(Cake.serving_size(7))  # Output: "Medium - Serves 5-8"
```

### Characteristics of Static Methods
- **Namespace Organization:** Static methods keep methods logically associated with a class within the class's namespace.
- **Memory Efficiency:** They don't require an instance to be created to be called, which can be more memory-efficient.
- **Limited Access:** They cannot modify or access the properties of the class or instances of the class.

### Comparison with Class Methods and Instance Methods
**Class Methods:**
- Can access and modify class state.
- Receive the class as the implicit first argument (cls).

**Instance Methods:**
- Can access and modify instance state and class state.
- Receive the instance as the implicit first argument (self).

**Static Methods:**
- Do not access or modify instance or class state.
- Do not receive an implicit first argument.

Static methods are best used when you need a utility function that doesn't access any properties of a class but still makes sense to be included within the class's scope, as it's closely related to the class's purpose. 
This keeps the class self-contained and easier to understand and maintain.

## Private Members
- Private members in object-oriented programming (OOP) are attributes or methods of a class that are not accessible or visible to the outside of the class. 
- They're meant to be strictly used internally within the class. 
- This encapsulation is a core concept of OOP, aimed at creating a clear interface and preventing external entities from accessing the internal workings of a class directly. 
- Let's delve into this concept in Python, noting that Python's approach to privacy is based on a naming convention.

### Private Instance Variables:
- In Python, private instance variables are created by prefixing the variable name with two underscore characters (__).
- However, it's important to note that this doesn't enforce strict privacy but is more of a convention to indicate that the variable is meant to be private. 
- Here's an example:
```python
class Cake:
    def __init__(self, flavor, secret_sauce):
        self.flavor = flavor  # Public variable
        self.__secret_sauce = secret_sauce  # Private variable

    def get_secret_sauce(self):
        return self.__secret_sauce  # Accessing the private variable within the class

cake = Cake("Chocolate", 'abc')
print(cake.flavor)  # This will work, as flavor is public
print(cake.__secret_sauce)  # This will raise an error, as secret sauce is private
```
In the Cake class:
- `flavor` is a **public variable**, accessible from outside the class.
- `__secret_sauce` is a **private variable**, not intended to be accessed or modified directly from outside the class.

### Private Methods:
- Similarly, private methods are defined by prefixing the method name with two underscores. 
- They are meant to be called only within the class and not meant to be accessible from instances of the class or subclasses.

```python
class Cake:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.__mix_ingredients()

    def __mix_ingredients(self):
        print("Mixing ingredients: ", self.ingredients)

cake = Cake(["flour", "sugar", "eggs"])
cake.__mix_ingredients()  # This will raise an error, as it's a private method
```
- Here, `__mix_ingredients` is a private method and is used internally by the `__init__` method.

### Name Mangling:
- In Python, private members are subject to **name mangling**. 
- The interpreter changes the name of the private attribute in a way that makes it harder to access unintentionally. 
- The new name is constructed by adding _ClassName before the attribute name.
- However, it's still possible to access private variables using name mangling:
```python
print(cake.__secret_sauce)  # This will raise an error, as secret sauce is private
print(cake._Cake__secret_sauce)  # This will work, but it's highly discouraged as it breaks the convention of private members.
```

# Inheritance
- Inheritance is a fundamental concept in object-oriented programming (OOP), allowing one class to inherit attributes and methods from another. 
- In Python, inheritance is used to create a new class that is a modified version of an existing class. 
- This promotes code reuse and establishes a hierarchical relationship between classes.

### Basic Concept of Inheritance
- **Base Class (Parent Class):** The class whose properties and methods are inherited.
- **Derived Class (Child Class):** The class that inherits properties and methods from the base class.

### Advantages of Inheritance
- **Code Reuse:** Common functionality can be written in the base class and specialized in the derived class.
- **Easy Maintenance:** Changes in the base class automatically propagate to derived classes, assuming they don't override base class methods.
- **Polymorphism:** A derived class can be treated as an instance of the base class, often useful in polymorphic behavior.

### Implementing Inheritance in Python
```python
# Base class
class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

    def bake(self):
        print(f"Baking a {self.flavor} cake!")

# Derived class
class WeddingCake(Cake):
    def __init__(self, flavor, tiers):
        super().__init__(flavor)  # Call the __init__ of the base class
        self.tiers = tiers

    def bake(self):
        print(f"Baking a {self.tiers}-tier {self.flavor} wedding cake!")
```
In this example:
- `WeddingCake` inherits from `Cake`.
- `WeddingCake` calls the `__init__` method of `Cake` using `super().__init__(flavor)` to ensure the flavor attribute is set.
- `WeddingCake` has its own attribute `tiers`.
- `WeddingCake` overrides the `bake` method to provide a specialized message for a wedding cake.


### Types of Inheritance
1. **Single Inheritance:** A derived class inherits from one base class.
2. **Multiple Inheritance:** A derived class inherits from multiple base classes.
3. **Multilevel Inheritance:** A class inherits from a derived class, making it a base class for a new class.
4. **Hierarchical Inheritance:** Multiple classes inherit from a single base class.
5. **Hybrid Inheritance:** A combination of multiple and multilevel inheritance.

### Method Resolution Order (MRO)
- In cases of multiple inheritance, Python uses the **Method Resolution Order (MRO)** to determine the order in which base classes are searched when looking for a method. 
- This is important to understand when you have complex inheritance hierarchies and need to know how Python will find the correct method to use.

### super() Function
- `super()` is used to call methods from the base class:
- In single inheritance, it's straightforward: super() refers to the base class.
- In multiple inheritance, super() follows the MRO to determine the next class to look for methods.


### Single Inheritance
- A derived class inherits from one base class.
```python
class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

class WeddingCake(Cake):
    def __init__(self, flavor, tiers):
        super().__init__(flavor)
        self.tiers = tiers

# Usage
cake = WeddingCake("Vanilla", 3)
print(cake.flavor)  # Output: Vanilla
```

### Multiple Inheritance
A derived class inherits from multiple base classes.

```python
class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

class Frosting:
    def __init__(self, frosting_type):
        self.frosting_type = frosting_type

class FrostedCake(Cake, Frosting):
    def __init__(self, flavor, frosting_type):
        Cake.__init__(self, flavor)
        Frosting.__init__(self, frosting_type)

# Usage
frosted_cake = FrostedCake("Chocolate", "Buttercream")
print(frosted_cake.flavor, frosted_cake.frosting_type)  # Output: Chocolate Buttercream
```

### Multilevel Inheritance
- A class inherits from a derived class, making it a base class for a new class.
```python
class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

class WeddingCake(Cake):
    def __init__(self, flavor, tiers):
        super().__init__(flavor)
        self.tiers = tiers

class DecoratedWeddingCake(WeddingCake):
    def __init__(self, flavor, tiers, decorations):
        super().__init__(flavor, tiers)
        self.decorations = decorations

# Usage
decorated_cake = DecoratedWeddingCake("Vanilla", 3, "Flowers")
print(decorated_cake.flavor, decorated_cake.tiers, decorated_cake.decorations)  # Output: Vanilla 3 Flowers
```

### Hierarchical Inheritance
- Multiple classes inherit from a single base class.
```python
class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

class WeddingCake(Cake):
    def __init__(self, flavor, tiers):
        super().__init__(flavor)
        self.tiers = tiers

class BirthdayCake(Cake):
    def __init__(self, flavor, candles):
        super().__init__(flavor)
        self.candles = candles

# Usage
wedding_cake = WeddingCake("Vanilla", 3)
birthday_cake = BirthdayCake("Chocolate", 24)
print(wedding_cake.flavor, wedding_cake.tiers)  # Output: Vanilla 3
print(birthday_cake.flavor, birthday_cake.candles)  # Output: Chocolate 24
```

### Hybrid Inheritance
- A combination of multiple and multilevel inheritance.
```python
class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

class Frosting:
    def __init__(self, frosting_type):
        self.frosting_type = frosting_type

class FrostedCake(Cake, Frosting):
    def __init__(self, flavor, frosting_type):
        Cake.__init__(self, flavor)
        Frosting.__init__(self, frosting_type)

class WeddingFrostedCake(FrostedCake):
    def __init__(self, flavor, frosting_type, tiers):
        super().__init__(flavor, frosting_type)
        self.tiers = tiers

# Usage
wedding_frosted_cake = WeddingFrostedCake("Red Velvet", "Cream Cheese", 4)
print(wedding_frosted_cake.flavor, wedding_frosted_cake.frosting_type, wedding_frosted_cake.tiers)  # Output: Red Velvet Cream Cheese 4
```

### Method Overriding
- A derived class can provide a specific implementation of a method that is already defined in its base class. 
- This is known as method overriding. 
- In the `WeddingCake` example, the `bake` method is overridden to provide a custom implementation for WeddingCake.

## Abstract Classes and Methods
- Abstract classes and methods are fundamental concepts in object-oriented programming, enabling you to create a **blueprint for other classes**. 
- They're particularly useful when you want to define a template for a group of subclasses and ensure they all follow the same structure or interface.

###  Abstract Classes:
- An abstract class is a class that cannot be instantiated on its own. 
- Instead, it is designed to be subclassed by other classes. 
- Abstract classes are used to define a common interface for a set of subclasses.

### Characteristics of Abstract Classes:
- **Cannot be Instantiated:** You cannot create an instance of an abstract class directly.
- **Subclassing Required:** They are meant to be base classes, which need to be extended by other subclasses.
- **Common Interface:** Abstract classes provide a way to define methods that must be created within any child classes built from the abstract class.

### Abstract Methods:
- An abstract method is a method that is declared in the abstract class but it does not have an implementation. 
- Subclasses are expected to implement this method.

### Characteristics of Abstract Methods:
- **Declaration Only:** An abstract method is declared but contains no implementation. Subclasses are expected to provide an implementation of this method.
- **Enforces Structure in Subclasses:** If a subclass inherits from an abstract class, it must implement all abstract methods of the parent class.

### Implementing Abstract Classes and Methods in Python:
- Python provides the `abc` module (**Abstract Base Classes**) to use abstract classes and methods. 
- Here's how you can create an abstract class and abstract methods:
```python
from abc import ABC, abstractmethod

class Cake(ABC):
    
    def __init__(self, flavor):
        self.flavor = flavor

    @abstractmethod
    def serve(self):
        pass

class Cupcake(Cake):
    def serve(self):
        return f"Serving a {self.flavor} cupcake."

class Pancake(Cake):
    def serve(self):
        return f"Serving a stack of {self.flavor} pancakes."
```
In this example:
- `Cake` is an **abstract class** because it contains the abstract method `serve`.
- `serve` is an abstract method. It's declared by using the `@abstractmethod` decorator, and it defines the method signature without an implementation.
- `Cupcake` and `Pancake` are **concrete classes** that inherit from Cake and provide their own implementation of the serve method.

### Usage of Abstract Classes and Methods:
- **Ensuring Consistency:** Abstract classes ensure that all subclasses built from them implement the same set of methods.
- **Design and Planning:** They are excellent for designing and planning your code, especially in large projects where you need a clear and consistent structure.
- **Preventing Instantiation:** Making a class abstract prevents it from being instantiated, which can be useful when you have a class that is designed only as a base class.
