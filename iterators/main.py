from iterators.sequence_iter import SequenceIterator
from utils import wrap_output, Options


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


@wrap_output
def run_sequence_iterator():
    sequence = [1, 2, 3]
    print("Running SequenceIterator with a `for` loop:")
    for item in SequenceIterator(sequence):
        print(f"Item: {item}")


def start_program():
    options = Options("Iterators")
    options.add_option("Run indefinite iteration with a `while` loop")
    options.add_option("Run definite iteration with a `for` loop")
    options.add_option("Run SequenceIterator with a `for` loop")

    while True:
        option = options.get_option()

        # raise ValueError(option)

        if option == "1":
            run_indefinite_iteration()
        elif option == "2":
            run_definite_iteration()
        elif option == "3":
            run_sequence_iterator()
        elif option.lower() == "x":
            break
