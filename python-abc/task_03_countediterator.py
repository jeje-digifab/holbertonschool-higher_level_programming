#!/usr/bin/python3
"""Module compiled with python3"""


class CountedIterator:
    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterator object and a counter.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """
        Override the __next__ method to increment the counter and fetch the
        next item.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")

    def get_count(self):
        """
        Return the current value of the counter.
        """
        return self.counter


if __name__ == "__main__":
    main()
