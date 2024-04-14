from iterators.main import start_program as start_iterators_program
from concurrency.main import start_program as start_concurrency_program
from utils import Options

if __name__ == '__main__':
    import sys
    from pathlib import Path

    # Add the current directory to sys.path so that the child
    # modules can import the parent modules:
    sys.path.append(str(Path(__file__).parent))

    options = Options("Main Menu")
    options.add_option("Iterators")
    options.add_option("Concurrency")

    while True:
        option = options.get_option()
        if option == "1":
            start_iterators_program()
        elif option == "2":
            start_concurrency_program()
        elif option.lower() == "x":
            print("Bye! Come back soon!")
            break
        else:
            print("Invalid option. Try again.")
