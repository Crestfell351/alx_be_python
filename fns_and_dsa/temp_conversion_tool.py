FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    fahrenheit = (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR + 32
    return fahrenheit

def convert_to_fahrenheit(celsius):
    celsius = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return celsius
temparature = input("Enter the temperature to convert: ")
cf = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")


if cf == 'C':
    new_temparature = convert_to_celsius(temparature) 
    print(f"{temparature(float)}°F is {new_temparature(float)}°C")
elif cf == 'F':
    new_temparature = convert_to_fahrenheit(temparature) 
    print(f"{temparature(float)}°C is {new_temparature(float)}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")
