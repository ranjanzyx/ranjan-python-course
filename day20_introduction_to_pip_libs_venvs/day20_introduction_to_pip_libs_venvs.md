# What is a Package Manager?
- Mobile App Store Analogy: Just as you use an app store to browse, install, or update apps on your smartphone, in Python, you use package managers like pip to manage your Python packages. 
- A package manager lets you install, update, or remove packages (collections of modules) easily, ensuring you have the right tools (apps) at your disposal for your programming projects.
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

## `pip download`
- `pip download` is a command used in the Python package management system that allows users to download packages without installing them. 
- This is particularly useful for creating offline repositories, analyzing package contents, or preparing for later installation.
- Key Features:
  - **Download Packages:** Fetches packages from PyPI or another Python package index without installing them.
  - **Dependency Resolution:** Resolves and downloads dependencies of the specified packages, ensuring that you have all required files for later installation.
- Usage:
  - To download a specific package: `pip download package_name`
  - To download a package with all its dependencies: `pip download package_name --dest /path/to/directory`

## Wheel Files
- Wheel files are a built-package format for Python, designed to replace the older `egg` format. 
- They have the `.whl` extension and offer several advantages:
- Advantages:
  - **Faster Installation:** Wheel files allow for faster installations compared to building from source, as they do not require execution of the setup.py script.
  - **Consistency:** Ensure consistent installations across platforms and machines.
  - **Compatibility:** Support for both pure Python and binary packages.
- **Naming Convention of Wheel Files**
  - The naming convention for wheel files is designed to convey key information about the package, including its version, compatibility, and build tags. 
  - The format is as follows: `{distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl`
    - **Distribution:** The name of the distributed package.
    - **Version:** The version of the package.
    - **Build Tag (optional):** A unique identifier when the same version of a package is built multiple times.
    - **Python Tag:** 
      - Indicates the version of Python the package is compatible with (e.g., cp37 for CPython 3.7).
      - Purpose: Indicates which Python implementation and version the wheel is compatible with.
      - Components: Usually composed of two parts - the implementation abbreviation and the version number.
      - Examples:
        - cp37: Indicates the wheel is for CPython version 3.7.
        - pp37: Indicates the wheel is for PyPy version 3.7.
    - **ABI Tag:** 
      - Purpose: Represents the ABI(**Application Binary Interface**) for which the wheel is compiled. 
      - The ABI dictates how the code interacts with the Python runtime.
      - Significance: Helps ensure binary compatibility, avoiding issues like segfaults or other incompatibilities due to differences in how binaries interact with different Python runtimes.
      - Examples:
        - cp37m: Indicates the wheel is built for CPython 3.7 with the pymalloc extension.
        - abi3: Represents a wheel compatible with Python 3.x ABI. It's designed for forward compatibility, meaning a wheel tagged with abi3 can be used with any Python version 3.x where x is greater than or equal to the minimum version for which it's built.
    - **Platform Tag:** The platform the wheel is compatible with (e.g., win_amd64 for Windows with AMD64 architecture).
- Example:
  - **numpy-1.21.2-cp39-cp39-win_amd64.whl**
  - This denotes a 
    - numpy package, 
    - version 1.21.2, 
    - for CPython 3.9, 
    - compatible with the cp39 ABI, 
    - on a Windows AMD64 architecture.

## Cross-Platform Compatibility of Wheel Files
- **Single Wheel File Compatible with All OS**
  - **Pure Python Wheel (Platform Independent):**
    - Example: `six-1.15.0-py2.py3-none-any.whl`
    - Interpretation: 
      - This is a wheel for the `six` package, 
      - version `1.15.0`. 
      - It's compatible with both Python 2 and Python 3 (py2.py3), 
      - does not require any specific ABI (none), and 
      - is platform-independent (any).
- **Different Wheel Files for Different OS**
  - In many cases, especially for packages with compiled extensions, you need different wheels for different operating systems:
  - **Linux:**
    - Example: `package_name-1.0.0-cp39-cp39-manylinux2014_x86_64.whl`
    - Interpretation: This wheel is for Python 3.9 on Linux, conforming to the manylinux2014 policy, compatible with x86_64 architecture.
    - Example: `numpy-1.19.5-cp38-cp38-manylinux1_x86_64.whl`
    - Interpretation: This wheel is for
      - numpy package, 
      - version 1.19.5, 
      - built for CPython 3.8 (cp38) on a 
      - Linux system adhering to the manylinux1 policy, 
      - compatible with x86_64 architecture.
  - **Windows:**
    - Example: `Twisted-20.3.0-cp38-cp38-win_amd64.whl`
    - Interpretation: This wheel is for the 
      - Twisted package, 
      - version 20.3.0, 
      - built for CPython 3.8 (cp38) on 
      - Windows, 
      - compatible with AMD64 architecture.
  - **macOS:**
    - Example: `matplotlib-3.3.4-cp39-cp39-macosx_10_9_x86_64.whl`
    - Interpretation: This wheel is for the 
      - matplotlib package, 
      - version 3.3.4, built for 
      - CPython 3.9 (cp39) on macOS, 
      - specifically for macOS version 10.9 (Mavericks) and later, 
      - compatible with x86_64 architecture.


### CPython vs. Python
- CPython and Python are terms that are often used interchangeably but have specific meanings:
- **Python:** 
  - Refers to the programming language itself, not to a specific implementation. 
  - It defines the syntax and semantics of the code you write.
- **CPython:** 
  - Is the default and most widely-used implementation of the Python language. 
  - It's the reference implementation that is developed by the Python Software Foundation and is written in C.
  - When people say "Python," they typically mean CPython because it's the most common implementation. 
  - However, there are other implementations like **PyPy** (known for its speed), **Jython** (Python for the Java platform), and **IronPython** (Python for the .NET platform), each with specific use cases and features.

### manylinux
- `manylinux` is a specification defining a standard platform for Python binary wheels on Linux. 
- The purpose of manylinux is to ensure that wheels built on one Linux system are compatible with many other Linux distributions.
- **Background:** 
  - Linux distributions can vary significantly in terms of the system libraries they include. 
  - This variability can lead to compatibility issues for Python wheels that include binary extensions.
- **Solution:** 
  - manylinux specifies a baseline of system libraries and versions (based on CentOS) that wheels must be built against to ensure broad compatibility.
- **Versions:** 
  - There are several versions of the manylinux standard (e.g., **manylinux1**, **manylinux2010**, **manylinux2014**, **manylinux_2_24**) 
  - Each version corresponds to a different set of system library versions. 
  - A wheel that is tagged with a manylinux standard is expected to work on many Linux distributions without requiring additional system dependencies.
### ABI (Application Binary Interface)
- The ABI is a specification that defines how data structures and functions are accessed in machine code, a level below the API (Application Programming Interface) which deals with source code. 
- In the context of Python wheels:
  - **Specific ABI:** 
    - When a wheel is built for a specific ABI, it means the compiled components of the wheel expect the Python interpreter to behave in a certain way, at a binary level. 
    - For example, they might rely on specific memory layouts or system calls.
    - Example: cp37m means the wheel is expecting CPython 3.7 with the pymalloc extension.
  - **Non-Specific ABI (none):** 
    - When a wheel specifies none for the ABI tag, it indicates that the wheel is not reliant on any particular ABI. 
    - This is typical for pure Python wheels that don't contain any compiled components. 
    - They are essentially platform-independent and can run on any Python interpreter without concern for the binary interface.
    - Example: The ABI tag none in `six-1.15.0-py2.py3-none-any.whl` indicates that the six package doesn't require a specific ABI.
- In summary, when a wheel doesn't require a specific ABI (none), it's usually because the package is pure Python code and doesn't include platform-specific binary extensions. 
- This makes it broadly compatible across different Python interpreters and platforms. 
- On the other hand, when a wheel is tied to a specific ABI, it's usually optimized for or dependent on the particularities of a specific Python interpreter and system environment.

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
      - `pip freeze`
      - Purpose and Functionality: 
        - **Snapshot of the Environment**: 
          - `pip freeze` generates a list of all installed packages in the current environment along with their exact versions. 
          - This list reflects the current state of the environment, acting as a snapshot.
        - **Requirements File Creation:** 
          - The typical usage of `pip freeze` is to create a `requirements.txt` file. 
          - This file serves as a manifest, detailing all the Python packages required to run a project. 
          - By running `pip freeze > requirements.txt`, you capture the environment's state.

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
### Understanding Virtual envs
- Let's again use the mobile App Store analogy.
- Imagine you have separate smartphones for personal use and work to avoid mixing up apps and settings. 
- In Python, virtualenv serves a similar purpose. 
- It creates isolated Python environments for different projects, ensuring the dependencies of one project don’t interfere with those of another. 
- Just like having a work phone with work-related apps and a personal phone with personal apps, virtualenv allows you to maintain separate environments/projects with their specific requirements and packages, avoiding conflicts and ensuring consistency.

- `venv` a built-in module for creating virtual environments.
- `venv` is included in Python 3.3 and later. 

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
- Let's again use the mobile app store analogy.
- **Modules (Individual Apps)**: 
  - In the world of Python, a module is like an individual app. 
  - Each module/app is designed to perform specific tasks or functions. 
  - For instance, a weather app provides weather forecasts; 
  - similarly, a Python module like datetime provides functionalities related to date and time.
- **Packages (App Categories/Folders):** 
  - Packages in Python are akin to categories or folders of apps in an app store. 
  - They organize related modules into a single collection under a common name, making it easier to find and use them. 
  - For example, the scipy package is a collection of modules for scientific and technical computing, just like a "Productivity" folder might contain your calendar, to-do list, and note-taking apps.
- **Libraries (Entire App Store):** 
  - A library in Python can be compared to the entire app store. 
  - It’s a comprehensive collection of modules and packages that provide a wide array of functionalities, much like how an app store offers a diverse range of apps for different purposes. 
  - Whether you're working on web development, data analysis, or any other task, you can find the necessary 'apps' (modules/packages) in this extensive 'app store' (library).
  
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


