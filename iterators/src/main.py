from iterators.src.sequence_iter import SequenceIterator
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


@wrap_output
def run_sequence_iterator():
    sequence = [1, 2, 3]
    print("Running SequenceIterator with a `for` loop:")
    for item in SequenceIterator(sequence):
        print(f"Item: {item}")


def print_options():
    print("[1] Run indefinite iteration with a `while` loop")
    print("[2] Run definite iteration with a `for` loop")
    print("[3] Run SequenceIterator with a `for` loop")
    print("[X] Exit")


def start_program():
    while True:
        print_options()
        value = input("Choose iterator option: ")
        if value == "1":
            run_indefinite_iteration()
        elif value == "2":
            run_definite_iteration()
        elif value == "3":
            run_sequence_iterator()
        elif value.lower() == "x":
            break
