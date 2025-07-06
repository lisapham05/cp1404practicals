class Guitar:
    """Represent a guitar with name, year of manufacturer, cost """
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of guitar """
        return f"{self.name} ({self.year}): ${self.cost:.2f}"


