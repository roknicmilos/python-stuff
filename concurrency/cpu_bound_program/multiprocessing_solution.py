import multiprocessing
import time

from concurrency.data import numbers


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums():
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


def run():
    start_time = time.time()
    print("Calculating with `multiprocessing`...")
    find_sums()
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
