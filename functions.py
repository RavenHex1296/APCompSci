chosen_conversion = input("Would you like to convert \n (A) Fahrenheit to Celsius \n (B) Celsius to Fahrenheit \n (C) Celcius to Kelvin \n (D) Kelvin to Celcius ")
input_value = float(input("What temperature would you like to input? \n Enter the letter of the option you want."))


def fahrenheit_to_celcius(input_temp):
    return (input_temp - 32) / 1.8


def celcius_to_fahrenheit(input_temp):
    return (input_temp * 1.8) + 32


def celcius_to_kelvin(input_temp):
    return input_temp + 273.15


def kelvin_to_celcius(input_temp):
    return input_temp - 273.15


if chosen_conversion == "A":
    print(str(input_value) + "° Fahrenheit is " + str(fahrenheit_to_celcius(input_value)) + "° Celcius")

elif chosen_conversion == "B":
    print(str(input_value) + "° Celcius is " + str(fahrenheit_to_celcius(input_value)) + "° Fahrenheit")

elif chosen_conversion == "C":
    print(str(input_value) + "° Celcius is " + str(fahrenheit_to_celcius(input_value)) + "° Kelvin")

elif chosen_conversion == "D":
    print(str(input_value) + "° Kelvin is " + str(fahrenheit_to_celcius(input_value)) + "° Celcius")