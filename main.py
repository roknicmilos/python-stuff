from iterators.main import start_program as start_iterators_program


def print_options():
    print("[1] Iterators")
    print("[X] Exit")


if __name__ == '__main__':
    import sys
    from pathlib import Path

    # Add the current directory to sys.path so that the child
    # modules can import the parent modules:
    sys.path.append(str(Path(__file__).parent))

    while True:
        print_options()
        value = input("Choose a program: ")
        if value == "1":
            start_iterators_program()
        elif value.lower() == "x":
            print("Bye! Come back soon!")
            break
        else:
            print("Invalid option. Try again.")
