# Iterators and Iterables

Python’s **iterators** and **iterables** are two different
but related tools that come in handy when you need to iterate
over a data stream or container.

- **Iterators** power and control the iteration process
- **iterables** typically hold data that you want to iterate
  over one value at a time.

Iterations can be categorized as **definite** and **indefinite**.

- **Indefinite** iterations, like those using a `while` loop, run
  for an unspecified number of times until a certain condition is
  met.
- **Definite** iterations, using a `for` loop, run a specified
  number of times based on the sequence they're iterating over.

## Iterators

A Python **object** is considered an iterator when it implements
**two special methods** collectively known as the **iterator
protocol**:

- `__iter__`: Called to initialize the iterator. It must return
  an iterator object.
- `__next__`: Called to iterate over the iterator. It must return
  the next value in the data stream. Used internally by `next()`
  function that allows you to traverse an iterator without a formal
  loop. This possibility can be helpful when you’re working with
  infinite iterators or with iterators that have an unknown number
  of items.

Python uses iterators under the hood to support every operation
that requires iteration, including `for` loops, comprehensions,
iterable unpacking, and more.

### Iterator Types

- Iterators that **yield original data** (example:
  [SequenceIterator](./iterators/sequence_iterator.py))
- Iterators that **yield transform data** (example:
  [SquareIterator](./iterators/square_iterator.py))
- Iterators that **yield generate data** (example:
  [FibonacciIterator](./iterators/fibonacci_iterator.py))

### Generators

Generator functions are special types of functions that allow you
to create iterators using a **functional style**.
The function-based iterator is way simpler and more straightforward
to write and understand compared to its class-based equivalent.

Check out [these generator examples](./iterators/generators.py).

### Memory Efficiency

Iterators and generators are **pretty memory-efficient** when you
compare them with regular functions, container data types, and
comprehensions.
With iterators and generators, you don’t need to store all the data
in memory (RAM) at the same time. Iterators **keep only one data
item in memory at a time**, generating the next items on demand or
**lazily**.

Another important memory-related difference between iterators,
functions, data structures, and comprehensions is that iterators
are the **only way to process infinite data streams**.

### Async Iterators

They are the same as regular iterators, except instead of using
iterator protocol methods, they use something we can call **async
iterator protocol**. This protocol is based on two methods:

- `__aiter__`: It must return an async iterator object.
- `__anext__`: It must return an awaitable object from a stream.
  It must raise a `StopAsyncIteration` exception when the iterator
  is exhausted.

## References
- [Iterators and Iterables in Python: Run Efficient Iterations](https://realpython.com/python-iterators-iterables/)