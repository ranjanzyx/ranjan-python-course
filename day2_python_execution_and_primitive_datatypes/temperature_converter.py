"""
Temperature Converter:
- Create a Python script that converts temperatures from Celsius to Fahrenheit and vice versa.
- Use float data types and ensure proper formatting of the output.
"""
celsius = input("Enter the temperature in celsius: ")
celsius = float(celsius)
converted_temperature_fahrenheit = (celsius * 9 / 5) + 32
print(round(converted_temperature_fahrenheit, 1))

fahrenheit = input("Enter the temperature in fahrenheit: ")
fahrenheit = float(fahrenheit)
converted_temperature_celsius = (fahrenheit - 32) * 5/9
print(round(converted_temperature_celsius, 1))
