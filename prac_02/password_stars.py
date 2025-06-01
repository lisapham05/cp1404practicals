MIN_LENGTH = 8

def main():
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print("Password too short")
        password = input("Enter password: ")
    print("*" * len(password))

main()

