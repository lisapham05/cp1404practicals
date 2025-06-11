"""
Sample output:
How many months? 5

Enter income for month 1: 120
Enter income for month 2: 245.4
Enter income for month 3: 900
Enter income for month 4: 1205.56
Enter income for month 5: 12.35

Income Report
-------------
Month  1 - Income: $    120.00         Total: $    120.00
Month  2 - Income: $    245.40         Total: $    365.40
Month  3 - Income: $    900.00         Total: $   1265.40
Month  4 - Income: $   1205.56         Total: $   2470.96
Month  5 - Income: $     12.35         Total: $   2483.31
"""

def main():
    number_of_months = int(input("How many months? "))
    incomes = []

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)

