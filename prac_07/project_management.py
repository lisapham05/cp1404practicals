"""
Project Management Program
Main program for managing projects

Estimated time: 1 hour
Actual Time:
"""

from project import Project
from datetime import datetime
import os

FILENAME = "projects.txt"

def load_projects(filename):
    """Load projects from file"""
    projects = []
    with open(filename, "r") as file:
        file.readline()
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 5:
                project = Project(*parts)
                projects.append(project)

    return projects

def save_projects(projects, filename):
    """Save projects to a file"""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

