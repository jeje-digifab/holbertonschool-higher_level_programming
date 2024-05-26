#!/usr/bin/python3
"""Module compiled with python3"""


class Fish:
    """
    Class representing a Fish.
    """

    def swim(self):
        """
        Method to make the fish swim.
        """
        print("The fish is swimming.")

    def habitat(self):
        """
        Method to describe the fish's habitat.
        """
        print("The fish lives in water.")


class Bird:
    """
    Class representing a Bird.
    """

    def fly(self):
        """
        Method to make the bird fly.
        """
        print("The bird is flying.")

    def habitat(self):
        """
        Method to describe the bird's habitat.
        """
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """
    Class representing a Flying Fish inheriting from both Fish and Bird.
    """

    def fly(self):
        """
        Method to make the flying fish soar.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Method to make the flying fish swim.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Method to describe the flying fish's habitat.
        """
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    main()
