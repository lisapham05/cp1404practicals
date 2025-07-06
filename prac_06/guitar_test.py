from guitar import Guitar

def test_guitar():
    """Test Guitar class"""
    current_year = 2025

    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    age_1 = current_year - 1922
    print(f"{guitar_1.name} get_age() - Expected {age_1}. Got {guitar_1.get_age()}")
    print(f"{guitar_1.name} is_vintage() - Expected True. Got {guitar_1.is_vintage()}")

    guitar_2 = Guitar("Another Guitar", 2013, 1000.00)
    age_2 = current_year - 2013
    print(f"{guitar_2.name} get_age() - Expected {age_2}. Got {guitar_2.get_age()}")
    print(f"{guitar_2.name} is_vintage() - Expected False. Got {guitar_2.is_vintage()}")

test_guitar()