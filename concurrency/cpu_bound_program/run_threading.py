import concurrent.futures
import time

from data import numbers


def cpu_bound(number):
    return sum(i * i for i in range(number))


def calculate_sums():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cpu_bound, numbers)


if __name__ == "__main__":
    start_time = time.time()
    print("Calculating...")
    calculate_sums()
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
