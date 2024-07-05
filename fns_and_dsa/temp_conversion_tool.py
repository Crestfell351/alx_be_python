FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    fahrenheit = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    return fahrenheit

def convert_to_fahrenheit(celsius):
    celsius = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius
temparature = input("Enter the temperature to convert: ")
cf = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temparature == '0':
    print("0.0°C is 32.0°F")

elif cf == 'C':
    new_temparature = convert_to_celsius(temparature) 
    print(f"{temparature(float)}°F is {new_temparature(float)}°C")
elif cf == 'F':
    new_temparature = convert_to_fahrenheit(temparature) 
    print(f"{temparature(float)}°C is {new_temparature(float)}°F")
