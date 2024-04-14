from concurrency.io_bound_program.unoptimized import run as run_unoptimized
from concurrency.io_bound_program.threading_solution import run as run_threading
from concurrency.io_bound_program.asyncio_solution import run as run_asyncio
from concurrency.io_bound_program.multiprocessing_solution import (
    run as run_multiprocessing
)
from utils import wrap_output, Options


def start_program():
    options = Options("I/O Bound Program")
    options.add_option("Run unoptimized I/O bound program")
    options.add_option("Run I/O bound program optimized with `threading`")
    options.add_option("Run I/O bound program optimized with `asyncio`")
    options.add_option("Run I/O bound program optimized with `multiprocessing`")

    while True:
        option = options.get_option()
        if option == "1":
            wrap_output(run_unoptimized)()
        elif option == "2":
            wrap_output(run_threading)()
        elif option == "3":
            wrap_output(run_asyncio)()
        elif option == "4":
            wrap_output(run_multiprocessing)()
        elif option.lower() == "x":
            break
