class Args:

    def __init__(self, *args):
        self.args = args
        self.verbose = self._parse_first_arg()

    def _parse_first_arg(self) -> bool:
        if len(self.args) < 2:
            return False

        first_arg = self.args[1]
        if first_arg == "-v":
            return True

        raise ValueError(f"Invalid argument {first_arg}")
