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

- Iterators that **yield original data** (example: [SequenceIterator](./sequence_iterator.py))
- Iterators that **yield transform data** (example: [SquareIterator](./square_iterator.py))
- Iterators that **yield generate data** (example: [FibonacciIterator](./fibonacci_iterator.py))
