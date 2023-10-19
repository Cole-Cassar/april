def celsius_to_fahrenheit():
    '''Calculates Celsius to Fahrenheit'''
    fah = 25 * 9/5 + 32
    return fah
# Program to convert Celcius to Fahrenheit
celsius = 25
fah = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees is {fah} Fahrenheit")