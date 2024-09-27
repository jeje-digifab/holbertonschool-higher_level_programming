#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    This class defines an abstract method 'sound' which must be implemented
    by all subclasses. Subclasses of Animal should provide their own
    implementation of the 'sound' method.
    """

    @abstractmethod
    def sound(self):
        """
        Returns the sound made by the animal.

        This method is implemented in each subclass to return
        the specific sound
        associated with the animal type. In the Dog class, it returns "Bark",
        and in the Cat class, it returns "Meow".

        Returns:
            str: The sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Dog class, subclass of Animal.

    This class implements the abstract method 'sound', returning the
    sound typically made by a dog: "Bark".
    """

    def sound(self):
        return ("Bark")


class Cat(Animal):
    """
    Cat class, subclass of Animal.

    This class implements the abstract method 'sound', returning the
    sound typically made by a cat: "Meow".
    """

    def sound(self):
        return ("Meow")
