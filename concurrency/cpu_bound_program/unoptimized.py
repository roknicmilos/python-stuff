import time

from concurrency.data import numbers


def cpu_bound(number):
    return sum(i * i for i in range(number))


def calculate_sums():
    for number in numbers:
        cpu_bound(number)


def run():
    start_time = time.time()
    print("Calculating without any optimization...")
    calculate_sums()
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
