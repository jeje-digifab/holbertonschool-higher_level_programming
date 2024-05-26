#!/usr/bin/python3
"""Module compiled with python3"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Define the abstract method sound that all subclasses must implement
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses to return the sound of
        the animal
        """
        pass


class Dog(Animal):
    """
    Implement the sound method for the Dog class to return "Bark"
    """

    def sound(self):
        """
        Return the sound made by the dog
        """
        return "Bark"


class Cat(Animal):
    """
    Implement the sound method for the Cat class to return "Meow"
    """

    def sound(self):
        """
        Return the sound made by the cat
        """
        return "Meow"


if __name__ == "__main__":
    main()
