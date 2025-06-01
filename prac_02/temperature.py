"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celcius_to_fahreheit()
        elif choice == "F":
            fahreheit_to_celsius()
        else:
            invalid_option()
    print("Thank you.")


def celcius_to_fahreheit():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")

def fahreheit_to_celsius():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} F")

def invalid_option():
    global choice
    print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()

main()
