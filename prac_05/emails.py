
def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.replace('.', ' ').replace('_', ' ').split()
    return ' '.join(parts).title()

def main():
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        email = input("Email: ").strip()

    default_name = get_name_from_email(email)
    confirmation = input(f"Is your name {default_name}? (Y/n) ").strip().lower()

    if confirmation == "" or confirmation == "y":
        name = default_name
    else:
        name = input("Name: "). strip()

    email_to_name[email] = name

for email, name in email_to_name.items():
    print(f"{name} ({email})")


