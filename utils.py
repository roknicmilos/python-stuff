from typing import Callable


def wrap_output(func):
    def wrapper(*args, **kwargs):
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        func(*args, **kwargs)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")

    return wrapper


class Options:

    def __init__(self, title: str):
        self._title = title
        self._options = []
        self._border = "=" * len(title)

    def add_option(self, text: str) -> None:
        self._options.append(text)
        if len(text) > len(self._border):
            self._border = "=" * len(text)

    def print(self) -> None:
        print(self._border)
        print(self._title)
        for i, text in enumerate(self._options, 1):
            print(f"[{i}] {text}")
        print("[X] Exit")
        print(self._border)

    def get_option(self) -> str:
        self.print()
        return input(f"{self._title} | Choose an option: ")
