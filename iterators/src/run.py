from utils import wrap_output


@wrap_output
def run_indefinite_iteration():
    print("Running INDEFINITE iteration with a `while` loop:")
    iteration = 0
    while iteration < 3:
        print(f"{iteration}. iteration")
        iteration += 1


@wrap_output
def run_definite_iteration():
    print("Running DEFINITE iteration with a `for` loop:")
    for iteration in range(3):
        print(f"{iteration}. iteration")


def print_options():
    print("1. Run indefinite iteration with a `while` loop")
    print("2. Run definite iteration with a `for` loop")
    print("3. Exit")


if __name__ == "__main__":
    while True:
        print_options()
        value = input("Enter the number of an option you want to run: ")
        if value == "1":
            run_indefinite_iteration()
        elif value == "2":
            run_definite_iteration()
        elif value == "3":
            print("Bye! Come back soon!")
            break
