
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    celcuis=float((temperature-32)*FAHRENHEIT_TO_CELSIUS_FACTOR)
    print(f'{temperature}°F is {celcuis}°C')

def convert_to_fahrenheit(celsius):
    fahrenheit=float(temperature*CELSIUS_TO_FAHRENHEIT_FACTOR+32)
    
    print(f'{temperature}°C is {fahrenheit}°F')

temperature=float(input("Enter a temperature: "))
sss=input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if sss=='C':
     convert_to_fahrenheit(celsius=temperature)
elif sss=='F':
    convert_to_celsius(fahrenheit=temperature)
else:
    raise ("Invalid temperature. Please enter a numeric value.")
    
