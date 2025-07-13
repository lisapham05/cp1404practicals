"""
Project Management Program
Main program for managing projects

Estimated time: 1 hour
Actual Time:
"""

from project import Project
from datetime import datetime

FILENAME = "projects.txt"

def main():
    """Main program to display menu"""
    print("Welcome to Pythonic Project Management")

    projects = load_projects(FILENAME)
    if projects:
        print(f"Loaded {len(projects)} projects from {FILENAME}")
    print_menu()

    choice = input(">>> ")
    while choice != 'q':
        print_menu()
        choice = input(">>> ").lower()

    if choice == 'l':
        filename = input("Filename: ")
        load_projects(filename)

    elif choice == 's':
        filename = input("Filename: ")
        save_projects(projects, filename)

    elif choice == 'd':
        display_projects(projects)

    elif choice == 'd':
        display_projects(projects)

    elif choice == 'f':
        filter_projects_by_date(projects)

    elif choice == 'a':
        project = add_new_project()
        projects.append(project)

    elif choice == 'u':
        update_project(projects)

    elif choice == 'q':
        save = input(f"Would you like to save to {FILENAME}? ").lower()
        if save in ['yes', 'y']:
            save_projects(projects, FILENAME)
        print("Thank you for using custom-built project management software.")
    else:
        print("Invalid option.")


def print_menu():
    """Print menu choices"""
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

def filter_projects_by_date(projects):
    """
    Filter and display projects that start after a user-specified date.
    """
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered = sorted([p for p in projects if p.start_after(filter_date)],
                          key=lambda x: x.start_date)
        for p in filtered:
            print(p)
    except ValueError:
        print("Invalid date format.")

def add_new_project():
    """
    Prompt the user to input new project details.
    """
    print("Let's add a new project")
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    percent = int(input("Percent complete: "))
    return Project(name, date_str, priority, cost, percent)

def update_project(projects):
    """
    Allow the user to select and update a project’s completion percentage and/or priority.
    """
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
        print(project)
        new_percent = input("New Percentage: ")
        new_priority = input("New Priority: ")
        if new_percent:
            project.completion_percentage = int(new_percent)
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid input.")

main()