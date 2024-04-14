import concurrent.futures
import time

from concurrency.data import numbers


def cpu_bound(number):
    return sum(i * i for i in range(number))


def calculate_sums():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cpu_bound, numbers)


def run():
    start_time = time.time()
    print("Calculating with `threading`...")
    calculate_sums()
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
