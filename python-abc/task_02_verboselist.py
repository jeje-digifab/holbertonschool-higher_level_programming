#!/usr/bin/python3
"""Module compiled with python3"""


class VerboseList(list):
    def append(self, item):
        """
        Print a message when an item is added to the list.
        """
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, items):
        """
        Print a message when the list is extended with multiple items.
        """
        print(f"Extended the list with [{len(items)}] items.")
        super().extend(items)

    def remove(self, item):
        """
        Print a message when an item is removed from the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        """
        Print a message when an item is popped from the list,
        either the last item if index is not specified,
        or the item at the specified index.
        """
        if index is None:
            print(f"Popped [{self[-1]}] from the list.")
            return super().pop()
        else:
            print(f"Popped [{self[index]}] from the list.")
            return super().pop(index)


if __name__ == "__main__":
    main()
