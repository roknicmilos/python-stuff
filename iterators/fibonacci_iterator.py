class FibonacciIterator:
    """
    Iterator that is GENERATING new data, Fibonacci numbers in this case.
    Takes no input data, generating new data as a result of some computation
    to finally yield the generated items.
    """

    def __init__(self, stop=10):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._stop:
            self._index += 1
            fib_number = self._current
            self._current, self._next = (
                self._next,
                self._current + self._next,
            )
            return fib_number
        else:
            raise StopIteration
