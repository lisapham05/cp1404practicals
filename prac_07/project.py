"""
Project Class Programm

Estimated time: 1 hour
Actual time:
"""

from datetime import datetime

class Project:
    """To represent a project with a name, start date, priority, cost estimate, and completion percentage."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """ Initialize Project"""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return string representation"""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")
