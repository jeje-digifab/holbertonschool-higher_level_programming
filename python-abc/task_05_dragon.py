#!/usr/bin/python3
"""Module compiled with python3"""


class SwimMixin:
    """
    A mixin class providing the ability to swim.
    """

    def swim(self):
        """
        Prints a message indicating that the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class providing the ability to fly.
    """

    def fly(self):
        """
        Prints a message indicating that the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon, inheriting from SwimMixin and FlyMixin.
    """

    def roar(self):
        """
        Prints a message indicating that the dragon roars.
        """
        print("The dragon roars!")


if __name__ == "__main__":
    main()
