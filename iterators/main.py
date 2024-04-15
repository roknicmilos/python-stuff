from iterators.fibonacci_iterator import FibonacciIterator
from iterators.generators import sequence_generator
from iterators.infinite_fibonacci_iterator import InfiniteFibonacciIterator
from iterators.sequence_iter import SequenceIterator
from iterators.square_iterator import SquareIterator
from utils import wrap_output, Options


@wrap_output
def run_indefinite_iteration():
    print("Running INDEFINITE iteration with a `while` loop:")
    iteration = 0
    while True:
        print(f"{iteration}. iteration")
        iteration += 1
        if iteration == 3:
            break


@wrap_output
def run_definite_iteration():
    print("Running DEFINITE iteration with a `for` loop:")
    for iteration in range(3):
        print(f"{iteration}. iteration")


@wrap_output
def run_sequence_iterator():
    print("Running SequenceIterator with a `for` loop:")
    for item in SequenceIterator([1, 2, 3]):
        print(f"Item: {item}")
    print(f"\nExplanation:{SequenceIterator.__doc__}")


@wrap_output
def run_square_iterator():
    print("Running SequenceIterator with a `for` loop:")
    for square in SquareIterator([1, 2, 3]):
        print(f"Item: {square}")
    print(f"\nExplanation:{SquareIterator.__doc__}")


@wrap_output
def run_fibonacci_iterator():
    print("Running FibonacciIterator with a `for` loop:")
    for number in FibonacciIterator():
        print(f"Item: {number}")
    print(f"\nExplanation:{FibonacciIterator.__doc__}")


@wrap_output
def run_infinite_fibonacci_iterator():
    print("Running InfiniteFibonacciIterator with a `for` loop:")
    for number in InfiniteFibonacciIterator():
        print(f"Item: {number}")


@wrap_output
def run_sequence_generator_iterator():
    print("Running sequence_generator with a `for` loop:")
    for number in sequence_generator([2, 4, 6]):
        print(f"Item: {number}")
    print(f"\nExplanation:{sequence_generator.__doc__}")


@wrap_output
def run_generator_expression_iterator():
    print("Running generator iterator created with generator expression:")
    generator_expression = (number for number in [2, 4, 6])
    for number in generator_expression:
        print(f"Item: {number}")


@wrap_output
def run_exhausted_generator_iterator():
    print("Running exhausted generator iterator with a `for` loop:")
    generator_expression = (number for number in [2, 4, 6])
    list(generator_expression)
    for number in generator_expression:
        print(f"Item: {number}")
    else:
        print("Generator is exhausted. There are no more items to yield.")


def start_program():
    options = Options("Iterators")
    options.add_option("Run indefinite iteration with a `while` loop")
    options.add_option("Run definite iteration with a `for` loop")
    options.add_option("Run SequenceIterator with a `for` loop")
    options.add_option("Run SquareIterator with a `for` loop")
    options.add_option("Run FibonacciIterator with a `for` loop")
    options.add_option("Run InfiniteFibonacciIterator with a `for` loop")
    options.add_option("Run sequence_generator with a `for` loop")
    options.add_option(
        "Run generator created with expression with a `for` loop"
    )
    options.add_option("Run exhausted generator iterator with a `for` loop")

    while True:
        option = options.get_option()
        if option == "1":
            run_indefinite_iteration()
        elif option == "2":
            run_definite_iteration()
        elif option == "3":
            run_sequence_iterator()
        elif option == "4":
            run_square_iterator()
        elif option == "5":
            run_fibonacci_iterator()
        elif option == "6":
            run_infinite_fibonacci_iterator()
        elif option == "7":
            run_sequence_generator_iterator()
        elif option == "8":
            run_generator_expression_iterator()
        elif option == "9":
            run_exhausted_generator_iterator()
        elif option.lower() == "x":
            break
