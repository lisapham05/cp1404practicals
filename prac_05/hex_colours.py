COLOUR_NAME_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "amber": "#ffbf00",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "baby blue": "#89cff0",
    "baby pink": "#f4c2c2",
    "bittersweet": "#fe6f5e",
    "bubble gum": "	#ffc1cc",
    "cambridge blue": "#a3c1ad",
    "camel": "#c19a6b"
}

for colour in COLOUR_NAME_TO_HEX:
    print(colour, end=" ")
print()

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_NAME_TO_HEX:
        print(f"{colour_name} is {COLOUR_NAME_TO_HEX[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").lower()