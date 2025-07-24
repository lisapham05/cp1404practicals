"""
CP1404 - Practical 09
Taxi Simulator
"""

from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """A taxi simulator program that uses Taxi and SilverServiceTaxi classes."""

    total_bill = 0
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

