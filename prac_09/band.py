"""
Band class
"""

class Band:
    """Represent a Band object, which consists of a collection of musicians."""

    def __init__(self, name=""):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band, including its musicians."""
        musician_details = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_details})"


    def add(self, musician: Musician):
        """Add a musician to the band."""
        self.musicians.append(musician)


