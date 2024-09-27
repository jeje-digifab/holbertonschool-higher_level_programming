#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


class VerboseList(list):
    """
    A custom list class that provides notifications for list modifications.
    """

    def append(self, item):
        """
        Append an item to the list and print a notification.

        Args:
            item: The item to be added to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with multiple items and print a notification.

        Args:
            item: An iterable whose items will be added to the list.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a notification.

        Args:
            item: The item to be removed from the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return an item at the given index and print a notification.

        Args:
            index: The position of the item to remove.
            Defaults to the last item.

        Returns:
            The removed item.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
