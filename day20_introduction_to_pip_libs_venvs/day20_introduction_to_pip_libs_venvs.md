# What is a Package Manager?
- A package manager is a tool that automates the process of installing, upgrading, configuring, and removing computer programs for a computer's operating system in a consistent manner. 
- It typically maintains a database of software dependencies and version information to prevent software mismatches and missing prerequisites.
- The underlying need for tools like package managers arises from the complexity in software development. 
- As projects grow, they often use code that other people have written, and managing this interdependency manually can become a nightmare. 
- These tools streamline the development process, reduce compatibility issues, and save developers a significant amount of time and effort, letting them focus on writing code rather than managing it.

## Why Do We Need Package Managers?
- **Dependency Management:** 
  - Software often depends on other software to work. 
  - Package managers keep track of what software needs to be installed for another piece of software to work.
- **Version Control:** 
  - They help manage different versions of software and allow users to install specific versions, which is crucial for compatibility and stability.
- **Ease of Installation:** 
  - Package managers automate the installation process, reducing the need for manual installations and the potential for human error.
- **Update Management:** 
  - They make it easier to update software to newer versions, often with a single command, ensuring that you have the latest features and security patches.

In Python, the concept of a package manager is implemented through tools like `pip` or `conda`.

# PyPi
- PyPI, short for the **Python Package Index**, is a repository of software for the Python programming language. 
- It serves a similar purpose for Python as what app stores do for mobile phones or what an app store like the Microsoft Store does for Windows. 
- Here are some key points about PyPI:
  - **Repository of Packages:** 
    - PyPI hosts tens of thousands of third-party Python packages. 
    - These packages can range from libraries to help with image processing, to packages designed for scientific computing, web development, and much more.
  - **Easy Package Installation:** 
    - PyPI is integrated with `pip`, a package installer for Python. 
    - This means that you can easily download and install Python packages from PyPI using simple commands in your command-line interface. 
    - For example, running pip install package-name would download and install a package from PyPI.
  - **Version Management:** 
    - PyPI allows authors to upload multiple versions of their packages. 
    - This is crucial for dependency management, ensuring that projects can specify the version of a package they require to avoid compatibility issues.

# PIP
- PIP stands for **"Pip Installs Packages"** or **"Pip Installs Python"** and is a package-management system used to install and manage software packages written in Python. 
- It connects to an online repository of public packages, called the **Python Package Index (PyPI)**, to download and install software.
- pip is included by default with Python versions 3.4 and above.

| Basic pip Commands          |                              |
|-----------------------------|------------------------------|
| Installing Packages         | `pip install package_name`   | 
| Uninstalling Packages       | `pip uninstall package_name` |
| Listing Installed Packages: | `pip list`                   |

# requirements.txt
- `requirements.txt` is used in python projects to specify the packages that a project depends on. 
- This file is commonly used in combination with `pip`, to install the necessary packages.

### Purpose:
  - **Dependency Management:** It lists all the Python libraries a project depends on
  - **Project Portability:** It makes your project portable and easier to set up on different environments (development, testing, production) by ensuring that the same versions of the libraries are installed everywhere.
  
### Creating requirements.txt
  1. **Manually:** 
      - You can manually create a requirements.txt file and list your dependencies. 
      - For each dependency, you can specify a version number, a version range, or leave it without a version to always get the latest version.
      - Example:
      ```makefile
      numpy==1.19.2
      pandas>=1.1.3
      scipy
      ```
  2. **Using pip freeze:** 
      - You can generate a requirements.txt file with all the packages installed in your current environment using the command:
      - `pip freeze > requirements.txt`

### Syntax and Specifications in requirements.txt
  - **Package Names:** The names of the packages as they are listed in PyPI.
  - **Version Specifiers:** You can specify versions using symbols like ==, >=, <=, >, <.
  - **Environment Markers:** 
    - Conditional dependencies based on the environment can be specified using environment markers. 
    - For instance, a package might only be required for a Windows environment.
    - Example:
      ```
      pywin32; platform_system == "Windows"
      ```
  - **Comment Lines:** Lines starting with `#` are treated as comments and are ignored.

### Using requirements.txt
- To install all the packages listed in requirements.txt, you use the command: `pip install -r requirements.txt`

### Best Practices
- **Specify Exact Versions:** It's generally a good idea to specify exact versions of your dependencies to avoid unexpected changes from updates.
- **Regularly Update:** Regularly update the dependencies to incorporate bug fixes and improvements, but do it cautiously to avoid breaking changes.
- **Minimize Dependencies:** Only include necessary dependencies to avoid bloating your project and potentially introducing conflicts or vulnerabilities.
In summary, requirements.txt is a vital tool for Python developers, streamlining the management of third-party libraries and ensuring consistency across different development and deployment environments.

```
# Exact version number (e.g., Django version 3.1.7)
Django==3.1.7

# No version specified (pip will install the latest version available)
requests

# Range of version numbers (e.g., Flask version >= 1.1.0 but < 2.0.0)
Flask>=1.1.0,<2.0.0

# Minimum version number (e.g., pandas version at least 1.2.3)
pandas>=1.2.3

# Package from a Git repository (e.g., a specific branch of a GitHub repo)
git+https://github.com/example_user/example_repo.git@dev_branch#egg=example_package

# A package that has dependencies on other packages (e.g., tensorflow)
tensorflow>=2.4.0

# A specific sub-dependency version (e.g., numpy version required by tensorflow)
numpy==1.19.5

# Another package with a minimum version number
scipy>=1.5.4

# A package with a version range
matplotlib>=3.3.0,<3.4.0

# mxnet for Linux (no version specified, so the latest version will be installed)
mxnet; platform_system == "Linux"

# mxnet-mkl for Windows (no version specified, so the latest version will be installed)
mxnet-mkl; platform_system == "Windows"
```

# `venv` - The Built-in Tool for creating virtual envs
- venv is included in Python 3.3 and later. 
- It's a built-in module for creating virtual environments.

| Task                             | Command                                                                         |
|----------------------------------|---------------------------------------------------------------------------------|
| Creating a Virtual Environment   | `python -m venv myenv`                                                          |
| Activating a Virtual Environment | Windows: `myenv\Scripts\activate` <br> macOS/Linux: `source myenv/bin/activate` |
| Deactivating a Virtual Environment | `deactivate`                                                                  |

### Understanding site-packages
- `site-packages` refers to a directory within the Python installation or virtual environment where third-party libraries and packages are installed. 
- These packages are typically not part of the Python standard library but are created and maintained by the Python community or third-party developers. 
- You use site-packages to store and manage external libraries and modules that can be imported and used in your Python programs.
  - **Directory Location:**
    - In a standard Python installation, the site-packages directory is usually located within the `lib` directory of the Python installation directory.
    - In virtual environments created using tools like venv or virtualenv, a separate site-packages directory is created within the virtual environment directory.
  - **Package Installation:**
    - When you install a Python package using a package manager like pip, the package and its associated files (modules, scripts, etc.) are placed in the site-packages directory.
    - For example, running the following command `pip install requests` installs a package named "requests" into the site-packages directory
  - **Importing Packages:**
    - After installing a package in the site-packages directory, you can import and use it in your Python code by using the import statement. `import requests`

### Additional Tools for Python Environment Management
- Other popular tools used for managing Python environments and dependencies. 
- These tools enhance or extend the capabilities provided by venv.
    1. **pyenv**: Mainly used to manage multiple Python versions on the same machine.
    2. **virtualenv**: A tool for creating isolated Python environments, similar to venv.
    3. **pipenv**: Aims to bring the best of all packaging worlds (bundling, version management) to the Python world.
    4. **poetry**: Tool for dependency management and packaging in Python.

# Understanding Libraries, Modules, Packages

## Module:
- It's a **single Python file** with a `.py` extension.
- Contains reusable code like classes, functions, and variables.
- Used to organize code and make it more manageable.
- Built-in Modules: `math`, `os`, `datetime`
- User-Defined Modules: A module you create, such as `my_module.py`, can contain functions and classes for your project.
- Imported using the `import` statement, e.g., `import math`.
- Example: The math module provides mathematical functions like `sqrt()` and `factorial()`.
```python
import math
print(math.sqrt(16))  # Output: 4.0
print(math.factorial(5))  # Output: 120
```

## Package:
- A collection of related modules, grouped together in a directory.
- Helps structure large projects and avoid naming conflicts.
- Must contain a special file called `__init__.py` to be recognized as a package.
- Example: The `requests` package provides tools for data analysis and manipulation.
```python
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    posts = response.json()
    for post in posts[:5]:
        print(f"Title: {post['title']}")
```

## Library:
- A broader term for a collection of modules and packages that provide specific functionality.
- Can be built-in (part of Python's standard library) or third-party (installed separately).
- Often used interchangeably with "package," but a library can be more extensive.
- Example: The NumPy library provides support for numerical computations.

### Key points:
- Modules are the building blocks of Python code.
- Packages organize modules into a hierarchical structure.
- Libraries offer reusable code for specific tasks.

### Visual analogy:
- Think of a module as a single book.
- A package is like a bookshelf containing multiple books related to a topic.
- A library is like a whole building full of bookshelves, covering diverse subjects.

```markdown
my_package/
    __init__.py
    module1.py
    module2.py
    sub_package/
        __init__.py
        module3.py
```

```python
# module1.py
def greet():
    return "Hello from module1!"
```

```python
# module2.py
def say_hello():
    return "Greetings from module2!"
```

```python
# sub_package/module3.py
def welcome():
    return "Welcome from module3 in sub_package!"
```

```python
# main.py

# Import module1 and module2 from my_package
import my_package.module1
from my_package import module2
# Import module3 from the sub-package
from my_package.sub_package import module3

# Use functions from the imported modules
print(my_package.module1.greet())  # Output: Hello from module1!
print(module2.say_hello())           # Output: Greetings from module2!
print(module3.welcome())            # Output: Welcome from module3 in sub_package!
```

# Practical Exercises
**TASK-1** 
- **Create a Module:** Create a module named `utilities.py` containing a few simple utility functions, like a function to calculate the average of a list of numbers.
- **Import and Use the Module:** Create a separate script where you import and use the functions from utilities.py module.

**TASK-2** 
- **Create and Activate:** Create a new virtual environment and activate it.
- **Install Packages:** install a simple package like `requests`
- **Write Script**: Write a simple script to fetch and display a list of to-do items from JSONPlaceholder (https://jsonplaceholder.typicode.com/todos).
- **Create a requirements.txt File:** Freeze and store current environment packages using pip freeze > requirements.txt.


