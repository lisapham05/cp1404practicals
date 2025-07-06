class Guitar:
    """Represent a guitar with name, year of manufacturer, cost """
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of guitar """
        return f"{self.name} ({self.year}): ${self.cost:.2f}"

    def get_age(self, current_year):
        """Return how old the guitar is in years"""
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is over 50 years or not"""
        return self.get_age() >= 50

