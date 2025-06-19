
def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.replace('.', ' ').replace('_', ' ').split()
    return ' '.join(parts).title()


