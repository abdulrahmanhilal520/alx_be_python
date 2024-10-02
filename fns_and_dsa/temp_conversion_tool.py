# temp_conversion_tool.py  

# Global Conversion Factors  
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  

def convert_to_celsius(fahrenheit):  
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  
    return celsius  

def convert_to_fahrenheit(celsius):  
    fahrenheit = (celsius *  CELSIUS_TO_FAHRENHEIT_FACTOR) + 32  
    return fahrenheit  

def main():  
    # User Interaction  
    try:  
        # Get temperature from user  
        temp_input = input("Enter the temperature to convert: ")  
        temp_value = float(temp_input)  # Convert the input to a float  
        
        # Ask for the unit of the temperature  
        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

        if unit_input == 'C':  
            # Convert Celsius to Fahrenheit  
            converted_temp = convert_to_fahrenheit(temp_value)  
            print(f"{temp_value}°C is {converted_temp}°F")  
        elif unit_input == 'F':  
            # Convert Fahrenheit to Celsius  
            converted_temp = convert_to_celsius(temp_value)  
            print(f"{temp_value}°F is {converted_temp}°C")  
        else:  
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")  
    
    except ValueError:  
        print("Invalid temperature. Please enter a numeric value.")  

# Entry point of the script  
if __name__ == "__main__":  
    main()
