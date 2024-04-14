from concurrency.io_bound_program.main import (
    start_program as start_io_bound_program
)
from concurrency.cpu_bound_program.main import (
    start_program as start_cpu_bound_program
)
from utils import Options


def start_program():
    options = Options("Concurrency")
    options.add_option("Run I/O bound program")
    options.add_option("Run CPU bound program")

    while True:
        option = options.get_option()
        if option == "1":
            start_io_bound_program()
        elif option == "2":
            start_cpu_bound_program()
        elif option.lower() == "x":
            break
