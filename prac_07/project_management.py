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

def main():
    """Main program to display menu"""
    print("Welcome to Pythonic Project Management")

    projects = load_projects(FILENAME)
    if projects:
        print(f"Loaded {len(projects)} projects from {FILENAME}")
    print_menu()



def print_menu():
    "Print menu choices"
    print("- (L)oad projects"
    "\n- (S)ave projects"
    "\n- (D)isplay projects"
    "\n- (F)ilter projects by date"
    "\n- (A)dd new project"
    "\n- (U)pdate project"
    "\n- (Q)uit")

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

def display_projects(projects):
    """Display incomplete and complete projects grouped and sorted by priority"""
    incomplete = sorted([p for p in projects if not p.is_complete()], key=lambda x: x.priority)
    complete = sorted([p for p in projects if p.is_complete()], key=lambda x: x.priority)
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")

print_menu()