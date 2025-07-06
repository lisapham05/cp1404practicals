"""
Program: programming_language.py

Estimated time: 30 minutes
Actual time: 17 minutes

"""

class ProgrammingLanguage:
    """Represents a programming language with characteristics"""

    def __init__(self, name, typing, reflection, year):
        """ Initialize a ProgrammingLanguage object """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """ Determine if the programming language is dynamically typed or not """
        return self.typing.lower()  == "dynamic"

    def __str__(self):
        """ Return a string representation of the ProgrammingLanguage object """
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"