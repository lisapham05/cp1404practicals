"""
CP1404/CP5632 Practical 09
SilverServiceTaxi class
"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes a flagfall and fanciness multiplier."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
