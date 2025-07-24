from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    reliable_car = UnreliableCar("Mostly Good", 100, 90)
    unreliable_car = UnreliableCar("Dodgy", 100, 9)

    print(f"Attempting to drive {reliable_car.name} and {unreliable_car.name} several times...")
    for i in range(1, 11):
        print(f"Attempt {i}:")
        print(f"{reliable_car.name} drove {reliable_car.drive(i)}km")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(i)}km")

#Final State of the car
    print(reliable_car)
    print(unreliable_car)

if __name__ == '__main__':
    main()