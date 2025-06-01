def main():
    score = get_valid_score()

    choice = ""
    while choice.upper() != "Q":
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_score_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print("*" * int(score))
        elif choice == "Q":
            print("Goodbye! Thanks for using the Score Evaluator.")
        else:
            print("Invalid option. Please choose again.")

def print_menu():
    print("\nMenu:")
    print("(G)et valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def get_valid_score():
    """Get a valid score between 0 and 100."""
    score = float(input("Enter a score (0–100): "))
    while score < 0 or score > 100:
        print("Invalid score. Try again.")
        score = float(input("Enter a score (0–100): "))
    return score

def get_score_result(score):
    """Return a result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()


