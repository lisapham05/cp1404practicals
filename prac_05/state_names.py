"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

#Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD":"Queensland", "NSW":"New South Wales", "NT":"Northern Territory", "WA":"Western Australia",
                "ACT":"Australian Capital Territory", "VIC":"Victoria", "TAS":"Tasmania", "SA":"South Australia"}

print(" ".join(CODE_TO_NAME.keys()))

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short states")
    state_code = input("Enter short state: ").upper()



