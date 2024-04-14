# Concurrency in Python

The dictionary definition of concurrency is simultaneous occurrence.
In Python, the things that are occurring simultaneously are called
by different names (thread, task, process) but at a high level, they
all refer to a sequence of instructions that run in order.

There are two types of programs/problems that can be solved using
concurrency:

- **I/O Bound Programs** - a program that frequently waits for
  input/output from some external source (e.g. a network, a disk, a
  user).
- **CPU Bound Programs** - a program that does a lot of computation.

## References

- [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/)