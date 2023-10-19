"""
    Program to convert Celsius to Fahrenheit
"""
def celsius_to_fahrenheit(celsius):
    '''Calculates Celsius to Fahrenheit'''
    fah = celsius * 9/5 + 32
    return fah

def fahrenheit_to_celsius(fahrenheit):
    celsius = fahrenheit - 32
    return celsius
# Program to convert Celcius to Fahrenheit
celsius = 25
fah = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees is {fah} Fahrenheit")

celsius = fahrenheit_to_celsius(fah)
print(f"{fah} degrees Fahrenheit is {celsius} Celsius")