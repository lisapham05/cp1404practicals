from taxi import Taxi

"""
CP1404/CP5632 Practical
Test Taxi class
"""

from taxi import Taxi

def main():
    """Test the Taxi class."""

    my_taxi = Taxi("Prius 1", 100, 1.23)

    my_taxi.drive(40)

    print("After first trip: ", my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}\n")

    my_taxi.start_fare()
    my_taxi.drive(100)

    print("After second trip: ", my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}\n")

main()
