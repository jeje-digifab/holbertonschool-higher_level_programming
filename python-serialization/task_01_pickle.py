#!/usr/bin/python3
"""Module compiled with python3"""

import pickle


class CustomObject:
    """
    A custom class that represents a person with a name, age, and student
    status.
    """

    def __init__(self, name=None, age=None, is_student=None):
        """
        Initialize the CustomObject with name, age, and is_student attributes.

        :param name: The name of the person (string).
        :param age: The age of the person (integer).
        :param is_student: The student status of the person (boolean).
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object in a formatted manner.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        :param filename: The name of the file where the object will be saved.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Error during serialization: {}".format(e))

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        :param filename: The name of the file from which the object will be
        loaded.
        :return: An instance of CustomObject if successful, None otherwise.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print("Error during deserialization: {}".format(e))
            return None


if __name__ == "__main__":
    # Create an instance of CustomObject
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object into a new instance
    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    new_obj.display()
