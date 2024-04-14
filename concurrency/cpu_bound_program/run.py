import time

from data import numbers


def cpu_bound(number):
    return sum(i * i for i in range(number))


def calculate_sums():
    for number in numbers:
        cpu_bound(number)


if __name__ == "__main__":
    start_time = time.time()
    print("Calculating...")
    calculate_sums()
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
