import os

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Check if the file containing conversion factors exists and is not empty
conversion_factors_file = "conversion_factors.txt"  # Replace with the actual file name
if os.path.exists(conversion_factors_file) and os.path.getsize(conversion_factors_file) > 0:
    # Read conversion factors from the file (if needed)
    with open(conversion_factors_file, "r") as f:
        # Process the file contents to extract conversion factors
        # ... (implementation depends on file format)

# ... (rest of the code remains the same)

temp_input = input("Enter the temperature to convert: ")
temp_value = float(temp_input)
unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if unit_input == 'C':
    fahrenheit = convert_to_fahrenheit(temp_value)
    print(f"{temp_value}°C is {fahrenheit}°F")
elif unit_input == 'F':
    celsius = convert_to_celsius(temp_value)
    print(f"{temp_value}°F is {celsius}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit ")
