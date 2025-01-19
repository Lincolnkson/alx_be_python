# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_ADJUSTMENT = 32

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius using global conversion factor.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit using global conversion factor.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    return 32 + celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

def get_valid_temperature():
    """
    Prompt user for a valid temperature value.
    
    Returns:
        float: Valid temperature value
        
    Raises:
        ValueError: If input is not a valid number
    """
    temp = input("Enter the temperature to convert: ")
    try:
        return float(temp)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def get_valid_unit():
    """
    Prompt user for a valid temperature unit (C/F).
    
    Returns:
        str: Valid unit ('C' or 'F')
        
    Raises:
        ValueError: If input is not 'C' or 'F'
    """
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if unit not in ['C', 'F']:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    return unit

def main():
    """
    Main function to run the temperature conversion tool.
    """
    try:
        # Get temperature and unit from user
        temperature = get_valid_temperature()
        unit = get_valid_unit()
        
        # Perform conversion based on input unit
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:  # unit == 'C'
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()