def wrap_output(func):
    def wrapper(*args, **kwargs):
        print("============================================================")
        func(*args, **kwargs)
        print("============================================================")

    return wrapper
