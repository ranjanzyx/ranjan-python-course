# Introduction to Data Science, AI, and ML

## What is Artificial Intelligence (AI)?
- **Understanding:** 
  - AI simulates human intelligence in machines. 
  - These machines are programmed to think like humans and **mimic their actions**, ultimately aiming to create systems capable of performing tasks requiring human-level intelligence.
  - These tasks include reasoning, perception, learning, and generalization. 
  - The ultimate goal of AI is to develop systems that can operate autonomously and adapt to new situations, much like a human would.
- **Branches of AI:** 
  - **robotics**: which focuses on developing machines capable of performing tasks in the physical world; 
  - **natural language processing (NLP)**, which deals with the interaction between computers and humans using natural language; and 
  - **computer vision**, which enables machines to interpret and understand visual information from the world.

## What is Machine Learning (ML)?
- **ML as a Subset of AI:** 
  - Machine Learning is a subset of AI 
  - It focuses on developing algorithms that enable computers to learn from and make decisions based on data. 
  - Unlike traditional programming, ML algorithms learn from data, improving their performance on a task with more experience.

### Types of ML: 
- There are three main types of machine learning:
- **Supervised learning:** 
  - The algorithm learns from labeled data, where each data point has a corresponding output.
- **Unsupervised learning:** 
  - The algorithm identifies patterns and structures in unlabeled data without any predefined output.
- **Reinforcement learning:** 
  - The algorithm learns through trial and error, interacting with an environment and receiving rewards for desired actions.

## What is Data Science?
- Data Science is an interdisciplinary field that employs scientific methods, processes, algorithms, and systems to extract knowledge and insights from both **structured and unstructured data**. 
- This data can come from various sources, like 
  - social media, 
  - sensors, and 
  - financial transactions.
- Data scientists utilize a wide array of tools and techniques to manipulate and analyze data.
- Tools like **Pandas** and **Numpy** are fundamental for data manipulation and analysis in Python to uncover patterns and trends. 
- Techniques such as **machine learning**, **statistical analysis**, and **data visualization** are pivotal in uncovering patterns, making predictions, and deriving insights from data.

## The Relationship Between Data Science, AI, and ML
- **Interconnectedness:** 
  - Data Science, AI, and ML are interconnected fields. 
  - Data Science provides the insights, AI focuses on creating intelligent systems capable of performing tasks that typically require human intelligence, and ML offers the methods for computers to learn from data. 
  - Together, they enable the development of advanced, intelligent systems.
- **Real-world Applications:** 
  - These technologies come together in various real-world applications, such as 
    - recommendation systems used by Netflix and Amazon, 
    - autonomous vehicles, and 
    - speech recognition systems like Siri and Alexa. 
  - They are transforming industries by enabling personalized experiences, automating tasks, and improving decision-making processes.


### What Do Data Scientists Do?
- **Roles and Responsibilities:** 
  - Data scientists are involved in a variety of tasks, including 
    - collecting and cleaning data, 
    - performing exploratory data analysis, 
    - building and testing predictive models, and 
    - communicating findings to stakeholders. 

- Their work is crucial in transforming raw data into actionable insights.

# Google Colab
- **Google Colab**, or **Google Colaboratory**, is a free cloud service hosted by Google that allows anyone to write and execute arbitrary Python code through the browser. 
- It's particularly popular among data scientists and AI researchers because it provides a way to use and share Jupyter notebooks without any setup required on the local machine. 
- One of the key features of Google Colab is that it offers free access to computing resources including GPUs and TPUs, which can significantly speed up computations necessary for large-scale data analysis and machine learning tasks. 
- Users can write, execute, and share their Python code directly in the browser, collaborate with others, and access their work from anywhere. 
- It's widely used for machine learning and data analysis projects, educational purposes, and research.

# NumPy
- NumPy (Numerical Python) is a foundational package for numerical computing in Python. 
- It provides support for large, multi-dimensional arrays and matrices, along with a large collection of mathematical functions to operate on these arrays.

## Why NumPy?
- Using NumPy over regular Python lists for numerical operations offers several advantages:
- **Performance:** NumPy operations are implemented in C, making them significantly faster than Python loops, especially for large arrays.
- **Memory Efficiency:** NumPy arrays are stored at one continuous place in memory unlike lists, making access faster.
- **Convenience:** NumPy provides a plethora of mathematical functions that can be applied directly to the entire array, making the code cleaner and more readable.
- **Functionality:** Beyond basic mathematical operations, NumPy supports more complex operations such as matrix multiplication, transposition, and high-level mathematical functions like linear algebra operations.

##  Difference Between Python List and NumPy Array
- **Type Safety:** 
  - Python lists can contain elements of different types. 
  - In contrast, NumPy arrays are homogeneous and all elements are of the same type, which is a key reason why NumPy can perform operations so efficiently.
- **Size:** 
  - Adding elements to a Python list can change its size. 
  - NumPy arrays have a fixed size at creation, changing the size of an ndarray will create a new array and delete the original.
- **Performance:** 
  - As mentioned, NumPy arrays provide significantly better performance for numerical operations due to their underlying implementation.
- **Functionality:** 
  - NumPy arrays come with a vast number of functions for complex mathematical operations, which are not available with standard Python lists.

**Regular Python List Operations Example**
```python
# Create a regular Python list
arr_list = [1, 2, 3, 4, 5]

# Basic operations using list comprehensions
print("Original list:", arr_list)

# for x in arr_list:
#     add_five.append(x + 5)
#     
print("Add 5 to each element:", [x + 5 for x in arr_list])  # Add 5 to each element
print("Multiply each element by 2:", [x * 2 for x in arr_list])  # Multiply each element by 2
print("Square each element:", [x ** 2 for x in arr_list])  # Square each element
```

**Numpy array Example**
```python
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])  # Efficient, fixed-type numerical array

# Basic operations
print("Original array:", arr)
# Vectorized operation: Adds 5 to each element, utilizing NumPy's efficiency
print("Add 5 to each element:", arr + 5)
# Vectorized operation: Multiplies each element by 2, more efficient than looping
print("Multiply each element by 2:", arr * 2)
# Vectorized operation: Squares each element, showcasing the ease of complex operations
print("Square each element:", arr ** 2)
```

```python
import numpy as np

# Creating a Numpy array
arr = np.array([1, 2, 3, 4, 5])

# Performing operations on the array
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
```


# Pandas (Panel Data)
- Pandas is a powerful library in Python used for **data manipulation and analysis**
- It provides **high-performance**, **easy-to-use data structures** and **data analysis tools**. 
- It's particularly suited for working with **structured data**, including data that is similar to what you would find in SQL tables or Excel spreadsheets. 
- The name "Pandas" is derived from "**Panel Data**", an econometrics term for **multidimensional structured data sets**.

## Key Features of Pandas
- **DataFrame Object:** 
  - At the heart of pandas is the DataFrame object, which is a two-dimensional labeled data structure with columns that can be of different types (e.g., float, int, boolean, and more). 
  - It's similar to a spreadsheet or SQL table.
- **Series Object:** 
  - A Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). 
  - It's essentially a single column of a DataFrame.
- **Handling Missing Data:** 
  - Pandas provides extensive support for handling missing data, including tools for filling in missing values, dropping them, or interpolating them.
- **Data Alignment:** 
  - Automatic and explicit data alignment is a core feature, meaning that you can work with data from different sources and pandas will align them for you, avoiding common mistakes.
- **GroupBy Functionality:** 
  - For grouping data and performing operations on these groups, similar to SQL group-by.
- **Powerful Data Manipulation:** 
  - Pandas allows for slicing, indexing, and subsetting large data sets. 
  - You can merge and join data sets with ease.
- **Time Series Functionality:** 
  - Pandas has simple, powerful, and efficient functionality for performing resampling operations during frequency conversion (e.g., converting secondly data into 5-minute data), window functions, moving window statistics, and more.
- **Easy Data Import/Export:** 
  - You can easily read and write data from and to different sources like CSV files, Microsoft Excel, SQL databases, and HDF5 format.

##  Why Use Pandas?
- **Data Cleaning and Preparation:** 
  - Data scientists spend a significant amount of time cleaning and preparing data. 
  - Pandas simplifies these tasks.
- **Data Analysis:** 
  - With its array of functions for statistical analysis, aggregation, and visualization, pandas is a powerful tool for analyzing data sets.
- **Data Visualization:** 
  - While not a primary focus of pandas itself, it integrates well with libraries like Matplotlib and Seaborn for data visualization, providing a seamless workflow.
- **Flexibility:** 
  - Pandas can handle a wide variety of data types, including heterogeneous data, time series data, and more.

Example-1: Basic Dataframe operations using Pandas
```python
# Importing the pandas library
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)

# Displaying the created DataFrame
print("Original DataFrame:")
print(df)
print("\n")  # New line for better readability

# Accessing a specific column: 'Name'
print("Accessing the 'Name' column:")
print(df['Name'])
print("\n")

# Accessing the first row using iloc
print("Accessing the first row:")
print(df.iloc[0])
print("\n")

# Adding a new column 'Employed' with boolean values
df['Employed'] = [True, False, True]
print("DataFrame after adding 'Employed' column:")
print(df)
print("\n")

# Modifying a value using .at[] (changing Alice's age to 26)
df.at[0, 'Age'] = 26
print("DataFrame after modifying Alice's age to 26:")
print(df)
print("\n")

# Filtering rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print("Filtered DataFrame (Age > 30):")
print(filtered_df)
print("\n")

# Computing and displaying summary statistics for numerical columns
print("Summary statistics for numerical columns:")
print(df.describe())
```

### Handling CSV files using Pandas
```python
import pandas as pd

# Step 1: Read data from CSV
df = pd.read_csv('sample_data.csv')
print("Original Data:")
print(df)
print("\n")

# Step 2: Modify the data
df['Age'] = df['Age'] + 1

# Step 3: Write data back to a new CSV
df.to_csv('modified_data.csv', index=False)

print("Data after modification written to 'modified_data.csv'.")
```
### Handling missing data using Pandas
- Handling missing values is a critical aspect of data preprocessing and analysis, particularly in real-world datasets where incomplete data can be common due to various factors such as errors in data collection, transmission losses, or intentional omission.

- **Identification of Missing Values**
  - Before handling missing values, it's essential to identify them. 
  - Pandas primarily uses **NaN (Not a Number)** to represent missing data, which is the default marker for missing values in floating-point arrays. 
  - However, in datasets, missing values could come in different forms, such as None, empty strings, or other placeholders like -999 or ?.
  - Pandas provides functions like **isna()** or **isnull()** to detect missing values across a DataFrame or Series.

- **Techniques for Handling Missing Values**
  - **1. Removing Missing Values:**
    - **dropna():** 
      - This method allows you to drop rows or columns that contain missing values. 
      - You can fine-tune it to drop rows where any or all of the values are missing, or similarly for columns. 
      - This approach is straightforward but may result in significant data loss, especially if many missing values are scattered throughout the data.
  - **2. Filling Missing Values:**
    - **fillna():** 
      - This method fills missing values with a specified value or a computed value such as the **mean, median, or mode** of the column.
      - You can also **forward-fill** (propagate the last valid observation forward) or **back-fill** (use the next valid observation to fill the gap).
  - **3. Interpolation:** 
    - For numerical data, interpolation methods can provide a more sophisticated approach to impute missing values based on surrounding data points. 
    - Pandas supports linear interpolation by default, but other methods are available, such as quadratic, polynomial, or spline interpolation, which can be more appropriate depending on the dataset's characteristics.
  - **4. Replacing Generic Values:**
    - **replace():** 
      - In cases where missing values are represented by placeholders (e.g., -999, None, or ?), the replace() method can be used to substitute these with NaN or other more meaningful values, making them easier to handle using standard Pandas functions.

```python
import pandas as pd
import numpy as np
from io import StringIO


# Simulating CSV data
csv_data = """Timestamp,City1,City2,City3
2024-02-01 00:00,20.5,19.8,21.1
2024-02-01 01:00,20.1,,21.5
2024-02-01 02:00,19.9,20.0,
2024-02-01 03:00,,19.5,21.0
2024-02-01 04:00,20.0,,20.9
2024-02-01 05:00,-999,19.8,
2024-02-01 06:00,20.2,,-999"""

df = pd.read_csv(StringIO(csv_data))

# Replacing -999 with np.nan to properly identify missing values
df.replace(-999, np.nan, inplace=True)

# Forward Fill
df_ffill = df.fillna(method='ffill')

# Displaying the original and handled DataFrames
print("Original DataFrame with placeholders replaced:")
print(df)
print("\nDataFrame after forward filling missing values:")
print(df_ffill)

# Original DataFrame with placeholders replaced:
#           Timestamp  City1  City2  City3
# 0  2024-02-01 00:00   20.5   19.8   21.1
# 1  2024-02-01 01:00   20.1    NaN   21.5
# 2  2024-02-01 02:00   19.9   20.0    NaN
# 3  2024-02-01 03:00    NaN   19.5   21.0
# 4  2024-02-01 04:00   20.0    NaN   20.9
# 5  2024-02-01 05:00    NaN   19.8    NaN
# 6  2024-02-01 06:00   20.2    NaN    NaN
# 
# DataFrame after forward filling missing values:
#           Timestamp  City1  City2  City3
# 0  2024-02-01 00:00   20.5   19.8   21.1
# 1  2024-02-01 01:00   20.1   19.8   21.5
# 2  2024-02-01 02:00   19.9   20.0   21.5
# 3  2024-02-01 03:00   19.9   19.5   21.0
# 4  2024-02-01 04:00   20.0   19.5   20.9
# 5  2024-02-01 05:00   20.0   19.8   20.9
# 6  2024-02-01 06:00   20.2   19.8   20.9
```

# Data Visualization
- Visualizing data is crucial for understanding the underlying patterns and making the information accessible to a broader audience. 
- Matplotlib and Seaborn are two popular Python libraries used for data visualization.

Matplotlib Example: Simple Line Chart

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

# Simulating CSV data
csv_data = """Timestamp,City1,City2,City3
2024-02-01 00:00,20.5,19.8,21.1
2024-02-01 01:00,20.1,,21.5
2024-02-01 02:00,19.9,20.0,
2024-02-01 03:00,,19.5,21.0
2024-02-01 04:00,20.0,,20.9
2024-02-01 05:00,-999,19.8,
2024-02-01 06:00,20.2,,-999"""

# Load CSV data into a DataFrame and replace placeholder values with NaN
df = pd.read_csv(StringIO(csv_data), parse_dates=['Timestamp'])
df.replace(-999, np.nan, inplace=True)

# Forward Fill
df_ffill = df.fillna(method='ffill')

# Data Visualization using Matplotlib
plt.figure(figsize=(10, 6))

# Plotting temperature trends for each city
for city in df_ffill.columns[1:]:  # Exclude Timestamp column
    plt.plot(df_ffill['Timestamp'], df_ffill[city], label=city)

# Adding labels and title
plt.xlabel('Timestamp')
plt.ylabel('Temperature')
plt.title('Temperature Trends for Each City')
plt.legend()

# Display the plot
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Handling incorrect/duplicate data in pandas**
```python
import pandas as pd
import numpy as np
from io import StringIO

# Simulating CSV data
csv_data = """Timestamp,City1,City2,City3
2024-02-01 00:00,20.5,19.8,21.1
2024-02-01 01:00,20.1,,21.5
2024-02-01 02:00,19.9,20.0,
2024-02-01 03:00,,19.5,21.0
2024-02-01 04:00,20.0,,20.9
2024-02-01 05:00,-999,19.8,
2024-02-01 06:00,20.2,,-999"""

# Load CSV data into a DataFrame and replace placeholder values with NaN
df = pd.read_csv(StringIO(csv_data), parse_dates=['Timestamp'])

# Replacing -999 with np.nan to properly identify missing values
df.replace(-999, np.nan, inplace=True)

# Handling Incorrect Data Types
if df['Timestamp'].dtype != 'datetime64[ns]':
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Handling Duplicates
df.drop_duplicates(inplace=True)

# Forward Fill
df_ffill = df.fillna(method='ffill')

# Displaying the original and handled DataFrames
print("Original DataFrame with placeholders replaced:")
print(df)
print("\nDataFrame after forward filling missing values:")
print(df_ffill)

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Grouping and Aggregation
print("\nAverage temperature for each city:")
print(df_ffill.mean())

# Filtering
print("\nRows where City1 temperature is greater than 20:")
print(df_ffill[df_ffill['City1'] > 20])

```

### Seaborn Example: Simple Data Visualization
- Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive and informative statistical graphics.
```python
import pandas as pd
import numpy as np
import seaborn as sns
from io import StringIO

# Simulating CSV data
csv_data = """Timestamp,City1,City2,City3
2024-02-01 00:00,20.5,19.8,21.1
2024-02-01 01:00,20.1,,21.5
2024-02-01 02:00,19.9,20.0,
2024-02-01 03:00,,19.5,21.0
2024-02-01 04:00,20.0,,20.9
2024-02-01 05:00,-999,19.8,
2024-02-01 06:00,20.2,,-999"""

# Load CSV data into a DataFrame and replace placeholder values with NaN
df = pd.read_csv(StringIO(csv_data), parse_dates=['Timestamp'])
df.replace(-999, np.nan, inplace=True)

# Forward Fill
df_ffill = df.fillna(method='ffill')

# Data Visualization using Seaborn
plt.figure(figsize=(10, 6))

# Plotting temperature trends for each city using Seaborn
sns.lineplot(data=df_ffill.drop(columns=['Timestamp']), dashes=False)

# Adding labels and title
plt.xlabel('Timestamp')
plt.ylabel('Temperature')
plt.title('Temperature Trends for Each City')

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

```

