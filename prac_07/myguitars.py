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



def load_guitars(filename):
    """Read guitars file and return list of Guitar objects"""
    guitars = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Display list of guitars with number in order"""
    if not guitars:
        print("No guitars to display.")
        return
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def add_new_guitars(guitars):
    """user add new guitars to the list."""
    print("Add new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
        except ValueError:
            print("Invalid input. Please enter a valid year and cost.")
            continue
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}): ${cost:.2f} added.")

def save_guitars(filename, guitars):
    """Write the list of guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == "__main__":
    main()
