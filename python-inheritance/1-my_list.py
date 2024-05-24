#!/usr/bin/python3
"""Module compiled with python3"""


class MyList(list):
    """
    Defines a subclass MyList that inherits from list.

    This subclass provides additional functionality to the list class.

    Not allowed to import any module.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.

        This method assumes all elements of the list are of type int.

        Not allowed to import any module.
        """
        sorted_list = sorted(self)
        print("{:}".format(sorted_list))


if __name__ == "__main__":
    main()
