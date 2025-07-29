import wikipedia

def main():
    user_search = input("Enter page title: ")

    while user_search:
        try:
            # Use auto_suggest=False to prevent automatic redirection
            # and to trigger the specific errors for "python" and "jcu".
            page = wikipedia.page(user_search, auto_suggest=False)

            # For a successful result, print title, summary, and URL
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{user_search}" does not match any pages. Try another id!')

        except wikipedia.exceptions.DisambiguationError as e:
            print(f'We need a more specific title. Try one of the following, or a new search:\n{e.options}')

        print()
        user_search = input("Enter page title: ")

    print("Thank you.")

if __name__ == '__main__':
    main()