# What is Concurrency?
- Concurrency is the ability of a system to deal with multiple tasks or operations at the same time. 
- It's a concept used in computing to improve the performance and efficiency of a program, especially when the program needs to handle many tasks that don't need to be executed in a sequential order. 
- Concurrency can be achieved in various ways, including `threading`, `multiprocessing`, and `asynchronous programming`. 
- The goal is to structure a program 
  - to take advantage of parallel hardware (like multi-core CPUs), or 
  - to improve responsiveness and performance when dealing with I/O-bound tasks or tasks that involve waiting for external events.

# Concurrency Illustrated: The Restaurant Analogy
- Now, let's understand these concepts with the restaurant analogy, envisioning a restaurant that employs different strategies to handle its operations concurrently:

## Sequential Execution (Non-concurrent):
- Imagine a chef working alone, handling tasks one after another: taking orders, cooking, serving, and cleaning. 
- This is akin to a non-concurrent Python program where tasks are executed one by one.

## Threading (Concurrency with GIL):
- The chef now has assistant chefs. 
- One takes orders, another cooks, another serves, and another cleans. 
- They work concurrently, but they're limited by the size of the kitchen; they can't all cook at the same time. 
- This represents Python threading: 
  - multiple threads can operate concurrently, but the GIL ensures only one executes at a time, 
  - making it ideal for I/O-bound tasks.

### Multiprocessing (Concurrency without GIL limitations):
- The restaurant expands, adding more kitchens with their chefs and teams, working independently on different orders. 
- This scenario mirrors Python multiprocessing, where each process has its interpreter and memory space
- This circumvents the GIL and fully utilizes multiple CPU cores for CPU-bound tasks.

### AsyncIO (Cooperative Concurrency):
- The chef is exceptionally organized, juggling multiple tasks efficiently, starting new ones while waiting for others to complete. 
- This is like Python's AsyncIO, a single-threaded, single-process model that handles concurrency by executing tasks cooperatively, perfect for I/O-bound tasks with lots of waiting.

- In summary, concurrency in Python, much like managing a busy restaurant, can be tackled in various ways. 
- Whether through threading, multiprocessing, or AsyncIO, Python offers a model to efficiently handle tasks, maximizing resource utilization and performance in different scenarios.

## CPU vs I/O Bound
### CPU-bound Tasks:
- **Description:** 
  - A task is said to be CPU-bound if it would go faster if the CPU were faster, 
  - i.e., the speed of the task is limited by the speed of the CPU.
  - These tasks benefit from **multiprocessing**, which utilizes multiple CPU cores by creating separate processes.
- **Examples:** 
  - Mathematical computation 
  - data analysis 
  - image processing.
### I/O-bound Tasks:
- **Description:** 
  - A task is I/O-bound if it spends more time waiting for I/O operations to complete than to complete its computation. 
  - That is, the speed of the task is limited by the speed of the I/O subsystem. 
  - These tasks benefit from **multithreading** or **asynchronous programming** because while one thread waits, another can execute, improving responsiveness.
- **Examples:** 
  - Web scraping 
  - file reading/writing 
  - network communication

# Types of Concurrency in Python:
- Despite the GIL, Python offers several ways to implement concurrency:
- **Threading:** Useful for I/O-bound tasks where the program spends a lot of time waiting for external events.
- **Multiprocessing:** Beneficial for CPU-bound tasks where you want to fully utilize multiple cores of the CPU, bypassing the GIL.
- **AsyncIO:** Suited for high-level structured network code, especially when dealing with many connections that are mostly waiting for I/O.

- Python supports various forms of concurrency, but it has some unique characteristics due to its design. 
- One of the most notable is the **Global Interpreter Lock (GIL)**, 
  - It is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. 
  - This means that in a multi-threaded Python program, even if there are multiple threads available, only one thread can execute Python code at a time.

## Global Interpreter Lock (GIL)
- **Definition:** 
  - The GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once in the standard Python interpreter (CPython). 
  - This means that even if you have multiple threads, only one thread can execute Python code at a time.
- **Implications:**
  - **CPU-bound tasks:** 
    - For CPU-bound tasks (tasks where the bottleneck is the CPU speed), the GIL can become a significant bottleneck because it prevents multi-core utilization. 
    - Even if you have multiple threads, only one thread can execute at a time, making multi-threading ineffective for CPU-bound tasks.
  - **I/O-bound tasks:** 
    - For I/O-bound tasks (tasks that spend time waiting for I/O operations like file access or network communication), the GIL is less of an issue. 
    - While one thread is waiting for I/O, another thread can take over the CPU.
- **Workarounds:**
  - Using the `multiprocessing` module to bypass the GIL by using separate processes instead of threads.
  - Using C extensions to perform computationally heavy tasks outside of the GIL.
  - Utilizing alternative Python interpreters that don't have a GIL, like Jython or IronPython.

---
# Processes and Threads

## Processes:
- **Definition:** 
  - A process is an instance of a program that is being executed. 
  - It contains the program code and its current activity. 
  - Each process has its own memory space and system resources.
- **Isolation:** 
  - Processes are fully isolated from each other, providing stability to the system. 
  - The failure of one process does not affect the others.
- **Communication:** 
  - Processes can communicate with each other through Inter-Process Communication (IPC) mechanisms like pipes, sockets, shared memory, etc.
- **Overhead:** 
  - Starting a process is heavyweight and more resource-intensive than starting a thread.

## Threads:
- **Definition:** 
  - A thread is a sequence of executable commands within a process. 
  - A process can have multiple threads running concurrently, sharing the same memory space and resources.
- **Shared Memory:** 
  - Threads within the same process share the same memory space, making the communication between them more straightforward. 
  - However, this also requires careful synchronization to avoid conflicts.
- **Overhead:** 
  - Threads are lighter than processes, requiring less memory and time to create and manage.
 

## Python Threading
- Threading in Python can be used for running multiple tasks or IO-bound function calls concurrently. 
- However, due to the GIL, only one thread can execute Python bytecode at once, so it's not useful for CPU-bound tasks.
- There are two ways of implementing threads:
  - `threading` module
  - `ThreadPoolExecutor` module

### `threading` module
```python
import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(.2)
        print(f"\nTID:{threading.get_ident()}: {i}", end="")

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()

# TID:25928: 1
# TID:25036: 1
# TID:25928: 2
# TID:25036: 2
# TID:25036: 3
# TID:25928: 3
# TID:25036: 4
# TID:25928: 4
# TID:25036: 5
# TID:25928: 5
```
### `ThreadPoolExecutor` Module
- `ThreadPoolExecutor`, introduced in Python 3.2 under the `concurrent.futures` module
- It is a higher-level interface for asynchronously executing callables. 
- It abstracts away the details of thread management, making it easier to work with threads. 
- It's particularly useful when you want to execute several tasks concurrently and manage a pool of threads.

- **Key Differences Between threading.Thread and ThreadPoolExecutor:**
  1. **Abstraction Level:** ThreadPoolExecutor provides a higher level of abstraction, allowing you to submit tasks without having to manage individual threads and their life cycles.
  2. **Ease of Use:** With ThreadPoolExecutor, you don't need to manually create, start, and join threads. Instead, you submit tasks to the pool, and it handles the thread lifecycle for you.
  3. **Resource Management:** ThreadPoolExecutor manages a pool of threads efficiently, reusing threads from the pool to execute tasks and reducing the overhead of thread creation.
  4. **Future Objects:** When you submit tasks to a ThreadPoolExecutor, you get a Future object that allows you to monitor the status of the task, wait for its completion, and obtain results.

```python
from concurrent.futures import ThreadPoolExecutor
import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(.2)
        print(f"\nTID:{threading.get_ident()}: {i}", end="")

# Creating a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as executor:
    # Submitting tasks to the executor
    future1 = executor.submit(print_numbers)
    future2 = executor.submit(print_numbers)

    # Waiting for the tasks to complete (optional, as 'with' block will wait for all tasks to complete)
    future1.result()
    future2.result()

# TID:11656: 1
# TID:35776: 1
# TID:35776: 2
# TID:11656: 2
# TID:35776: 3
# TID:11656: 3
# TID:11656: 4
# TID:35776: 4
# TID:35776: 5
# TID:11656: 5
```

## Python Multiprocessing
- Multiprocessing in Python is used to create separate processes for each task. 
- It's suitable for CPU-bound tasks as it bypasses the GIL and can utilize multiple CPU cores.
- There are two methods of implementing threads:
  - `multiprocessing` module
  - `ProcessPoolExecutor` module

### `multiprocessing` module
```python
import os
from multiprocessing import Process
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(0.3)
        print(f"PID:{os.getpid()}: {i}")


if __name__ == '__main__':
    # Creating processes
    process1 = Process(target=print_numbers)
    process2 = Process(target=print_numbers)

    # Starting processes
    process1.start()
    process2.start()

    # Waiting for processes to complete
    process1.join()
    process2.join()

# PID:25516: 1
# PID:27488: 1
# PID:25516: 2
# PID:27488: 2
# PID:25516: 3
# PID:27488: 3
# PID:25516: 4
# PID:27488: 4
# PID:25516: 5
# PID:27488: 5
```

### `ProcessPoolExecutor` module
```python
from concurrent.futures import ProcessPoolExecutor
import time
import os

def print_numbers():
    for i in range(1, 6):
        time.sleep(0.1)
        print(f"\nPID:{os.getpid()}: {i}", end="")

if __name__ == '__main__':
    # Creating a ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=2) as executor:
        # Scheduling the print_numbers function to be executed
        executor.submit(print_numbers)
        executor.submit(print_numbers)

# PID:25640: 1
# PID:35376: 1
# PID:25640: 2
# PID:35376: 2
# PID:25640: 3
# PID:35376: 3
# PID:25640: 4
# PID:35376: 4
# PID:25640: 5
# PID:35376: 5
```

**Example with both multiprocessing and multithreading**
```python
import os
import threading
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

def compute_square(number):
    pid = os.getpid()
    tid = threading.get_ident()
    result = number * number
    print(f"\nPID: {pid}, TID: {tid}, compute_square({number}) = {result}")
    time.sleep(.5)


def process_task(numbers):
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(compute_square, numbers)


if __name__ == '__main__':
    number_chunks = [[1, 2, 3], [4, 5, 6]]

    with ProcessPoolExecutor(max_workers=2) as executor:
        future_results = executor.map(process_task, number_chunks)

# PID: 27604, TID: 10392, compute_square(1) = 1
# PID: 27604, TID: 32744, compute_square(2) = 4
# PID: 27604, TID: 33748, compute_square(3) = 9
# PID: 27740, TID: 28068, compute_square(4) = 16
# PID: 27740, TID: 31564, compute_square(5) = 25
# PID: 27740, TID: 12284, compute_square(6) = 36
```
```
[Python Program]
│
├── Process 1 (PID: 27604) ── GIL for Process 1
│   │
│   ├── Thread 1 (TID: 10392)
│   ├── Thread 2 (TID: 32744)
│   └── Thread 3 (TID: 33748)
│
└── Process 2 (PID: 27740) ── GIL for Process 2
    │
    ├── Thread 1 (TID: 28068)
    ├── Thread 2 (TID: 31564)
    └── Thread 3 (TID: 12284)
```

### Explanation:
- **Processes:** 
  - Your program has two separate processes (Process 1 and Process 2), each created by ProcessPoolExecutor. 
  - Each process has its own Python interpreter and its own GIL.

- **Threads within Each Process:** 
  - Within each process, you have a ThreadPoolExecutor managing three threads. 
  - These threads share the same GIL within their respective processes.

- **GIL (Global Interpreter Lock):** 
  - Each process has its own GIL. 
  - The GIL ensures that in each process, only one thread can execute Python bytecodes at a time.
  - However, threads can still perform certain actions concurrently, like I/O operations or running C extensions that release the GIL.

- **Concurrency and Parallelism:**
  - **Concurrency in Threads:** 
    - Threads within the same process can run concurrently, especially for I/O-bound tasks or when the GIL is released during certain operations. 
    - However, for CPU-bound tasks, the GIL ensures that only one thread runs at a time.
- **Parallelism in Processes:** 
  - Each process runs in parallel because each one has its own Python interpreter and GIL. 
  - This allows your program to utilize multiple CPU cores effectively, especially for CPU-bound tasks.

# Asynchronous Programming in Python:
- Asynchronous programming in Python is a way to write concurrent code that can efficiently handle multiple tasks without blocking the execution of the entire program. 
- Traditionally, Python has been single-threaded, meaning it executes one task at a time. 
- However, there are situations where you may want to perform tasks concurrently, such as handling I/O-bound operations, network requests, or other tasks that involve waiting for external events.

- Asynchronous programming introduces the concept of **"coroutines",** which are special functions that can pause and resume their execution without blocking the entire program. 
- It allows you to write non-blocking code that can perform other tasks while waiting for I/O operations to complete. 
- Python's standard library provides the `asyncio` module to work with asynchronous programming.

## asyncio in Python:
- `asyncio` is a Python library introduced in Python 3.3 that provides a framework for asynchronous programming. 
- It allows you to write asynchronous code using the async and await keywords, making it easier to handle I/O-bound operations and other asynchronous tasks. Here are some key components of asyncio:

### 1. Coroutines: 
  - Asyncio uses asynchronous functions known as **coroutines**. 
  - You can define coroutines using the `async` keyword. 
  - Coroutines can be paused and resumed using the await keyword.
### 2. Event Loop: 
  - The event loop is the core of asyncio. 
  - It manages the execution of asynchronous tasks and coroutines, scheduling them to run when their dependencies are ready.
### 3. Async Functions: 
  - Functions marked with `async` are expected to yield control back to the event loop using await. 
  - This allows the event loop to continue processing other tasks while waiting for the asynchronous operation to complete.
### 4. I/O Operations: 
  - asyncio is particularly useful for I/O-bound operations, such as reading from files, making network requests, or interacting with databases, as it allows you to perform these operations asynchronously without blocking the main thread.
### 5. Concurrency: 
  - asyncio allows you to run multiple coroutines concurrently, making it suitable for building highly concurrent and scalable applications.

```python
import asyncio
import os
import threading
import time

async def compute_square(number):
    pid = os.getpid()
    tid = threading.get_ident()
    # Simulate some asynchronous work by sleeping for 0.5 seconds.
    time.sleep(0.5)
    result = number * number
    print(f"\nPID: {pid}, TID: {tid}, compute_square({number}) = {result}")


# This is a coroutine function that processes a list of numbers using the compute_square function
async def process_task(numbers):
    tasks = []
    for number in numbers:
        tasks.append(compute_square(number))
    # Use asyncio.gather to concurrently run multiple compute_square coroutines.
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    number_chunks = [[1, 2, 3], [4, 5, 6]]

    # Create a list of tasks, each representing the processing of a number chunk.
    tasks = []
    for chunk in number_chunks:
        tasks.append(process_task(chunk))
    print(tasks)
    
    # Get the event loop for asyncio.
    loop = asyncio.get_event_loop()
    # Run the event loop until all tasks are completed.
    loop.run_until_complete(asyncio.gather(*tasks))
    # Close the event loop.
    loop.close()
    
# [<coroutine object process_task at 0x0000016C61CCAA40>, <coroutine object process_task at 0x0000016C61CCACE0>]
# PID: 9048, TID: 14380, compute_square(1) = 1
# PID: 9048, TID: 14380, compute_square(2) = 4
# PID: 9048, TID: 14380, compute_square(3) = 9
# PID: 9048, TID: 14380, compute_square(4) = 16
# PID: 9048, TID: 14380, compute_square(5) = 25
# PID: 9048, TID: 14380, compute_square(6) = 36
```

| Feature           | Multithreading                   | Asyncio                                          |
|-------------------|----------------------------------|--------------------------------------------------|
| Threads           | Multiple                         | Single thread, multiple coroutines               |
| GIL Impact        | Significant                      | Minimized                                        |
| Ideal for         | I/O-bound tasks                  | Highly I/O-bound, potentially also CPU-bound     |
| Code style        | More complex                     | More concise, but relies on async/await keywords |
| Learning curve    | Steeper                          | Easier due to single-threaded nature             |
