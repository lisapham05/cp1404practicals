
def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.replace('.', ' ').replace('_', ' ').split()
    return ' '.join(parts).title()

def main():
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        email = input("Email: ").strip()



