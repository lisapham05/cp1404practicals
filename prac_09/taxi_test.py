from taxi import Taxi

"""
CP1404/CP5632 Practical
Test Taxi class
"""
from taxi import Taxi

def main():
    """Test the Taxi class."""
    PRICE_PER_KM = 1.23
    UNITS_OF_FUEL = 100

    my_taxi = Taxi("Prius 1", UNITS_OF_FUEL, PRICE_PER_KM)
    my_taxi.drive(40)

    print("After first trip: ", my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}\n")

    my_taxi.start_fare()
    my_taxi.drive(100)
