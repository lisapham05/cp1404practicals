"""
CP1404 : Prac 09
UnreliableCar Class
"""

from car import Car
from random import randint

class UnreliableCar(Car):
    """A specialised version of a Car that is not always reliable."""

    def __init__(self, name, fuel, reliability: float):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than its reliability."""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
