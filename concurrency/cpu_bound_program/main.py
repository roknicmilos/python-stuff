from concurrency.cpu_bound_program.unoptimized import run as run_unoptimized
from concurrency.cpu_bound_program.threading_solution import (
    run as run_threading
)
from concurrency.cpu_bound_program.multiprocessing_solution import (
    run as run_multiprocessing
)
from utils import wrap_output, Options


def start_program():
    options = Options("CPU Bound Program")
    options.add_option("Run unoptimized CPU bound program")
    options.add_option("Run CPU bound program optimized with `threading`")
    options.add_option("Run CPU bound program optimized with `multiprocessing`")

    while True:
        option = options.get_option()
        if option == "1":
            wrap_output(run_unoptimized)()
        elif option == "2":
            wrap_output(run_threading)()
        elif option == "3":
            wrap_output(run_multiprocessing)()
        elif option.lower() == "x":
            break
