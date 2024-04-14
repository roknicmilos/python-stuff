import multiprocessing
import time

from data import numbers


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums():
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


if __name__ == "__main__":
    start_time = time.time()
    print("Calculating...")
    find_sums()
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
