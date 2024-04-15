class SequenceIterator:
    """
    Iterator that is YIELDING the ORIGINAL data.
    Takes a stream of data and yields data items
    as they appear in the original data.
    """

    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        """
        Required `for` an iterator.
        """
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
