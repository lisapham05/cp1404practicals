"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9


# Use f-string formatting to produce the output:
# 1922 Gibson L-5 CES for about $16,036!
print(f"{year} {name} for about ${cost}!")


# Using a for loop with the range function and f-string formatting,
# produce the following right-aligned output (DO NOT use a list):
# 2 ^ 0 is    1
# 2 ^ 1 is    2
# 2 ^ 2 is    4
# 2 ^ 3 is    8
# 2 ^ 4 is   16
# 2 ^ 5 is   32
# 2 ^ 6 is   64
# 2 ^ 7 is  128
# 2 ^ 8 is  256
# 2 ^ 9 is  512
# 2 ^10 is 1024
for i in range(11):
    power_of_2 = 2 ** i
    print(f"2 ^ {i:<2} is {power_of_2:>4}")

