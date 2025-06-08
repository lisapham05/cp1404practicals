"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   When user enters input that cannot be converted to interger
   This happens when the int() function attempts to convert a string that does not represent a whole number
2. When will a ZeroDivisionError occur?
   If user enters 0 as the value for denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Yes
"""
#Given code:
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
"""
#Code change:
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")