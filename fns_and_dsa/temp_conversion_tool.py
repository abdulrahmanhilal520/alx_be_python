# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
  """Prompts the user for temperature conversion and displays the result."""
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

      if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        unit_label = "°C"
        result_unit = "°F"
      elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        unit_label = "°F"
        result_unit = "°C"
      else:
        print("Invalid unit. Please enter 'C' or 'F'.")
        continue

      print(f"{temperature}{unit_label} is {converted_temp:.2f}{result_unit}")
      break

    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
  main()
