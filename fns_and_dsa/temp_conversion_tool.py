FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


convert = float(input("Enter the temperature to convert: "))
choice =input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if choice.upper() == "C":
    celcius = convert_to_celsius(convert)
    print(f"{convert}°F is {celcius}°C.")
elif choice.upper() == "F":
    fahrenheit = convert_to_fahrenheit(convert)
    print(f"{convert}°C is {fahrenheit}°F.")
    
else:
    print("Invalid temperature. Please enter a numeric value.")
