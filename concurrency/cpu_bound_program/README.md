# Speeding up I/O Bound programs

This project has different implementation of the same functionality: 
___calculate SUM of a large number of numbers___

For these kinds of problems, using `threading` or `asyncio` will not 
help much. In fact, it will most likely slow down the program because
of the overhead of creating and managing threads/tasks.

## Unoptimized implementation

Run: 
```bash
python src/run.py
```

## Implementation with `threading`

Run: 
```bash
python src/run_threading.py
```

## Implementation with `multiprocessing`

Run: 
```bash
python src/run_multiprocessing.py
```
