import csv
from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Main program to display guitar list."""
    guitars = load_guitars(FILENAME)
    print("These are the guitars loaded from file:")
    display_guitars(guitars)

    guitars.sort()    #Sorting
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    add_new_guitars(guitars)     #Add new guitar
    guitars.sort()               #Sort again
    print("\nFinal list of guitars (sorted):")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"\nGuitars have been saved to {FILENAME}.")
