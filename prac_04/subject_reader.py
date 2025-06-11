"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subjects(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subject_data.append(parts)
    return subject_data

def display_subjects(data):
    for subjects, lecturer, number_students in data:
        print(f"{subjects} is taught by {lecturer} and has {number_students} students")

main()