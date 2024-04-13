# Speeding up I/O Bound programs

This project has different implementation of the same functionality: 
___downloading content from a big number of different websites___

Append `-v` flag to each of the below-mentioned commands for greater
verbosity.

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

## Implementation with `asyncio`

Run: 
```bash
python src/run_asyncio.py
```

## Implementation with `multiprocessing`

Run: 
```bash
python src/run_multiprocessing.py
```
