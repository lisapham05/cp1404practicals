from guitar import Guitar

def test_guitar():
    """Test Guitar class"""
    current_year = 2025

    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    age_1 = current_year - 1922
    print(f"{guitar_1.name} get_age() - Expected {age_1}. Got {guitar_1.get_age()}")
    print(f"{guitar_1.name} is_vintage() - Expected True. Got {guitar_1.is_vintage()}")

