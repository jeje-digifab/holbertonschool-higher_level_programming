# Python - Inheritance

This project focuses on understanding Python inheritance, including classes, attributes, and methods. The tasks involve creating classes and functions that demonstrate the principles of object-oriented programming (OOP) in Python.

## Tasks

### 0. Lookup
**Description:**
Write a function `lookup` that returns the list of available attributes and methods of an object.

- **Prototype:** `def lookup(obj):`
- **Returns:** A list of attributes and methods of the object.
- **No external modules allowed.**

**File:** `0-lookup.py`

### 1. My list
**Description:**
Create a class `MyList` that inherits from `list`. Add a method `print_sorted` that prints the list sorted in ascending order.

- **Method:** `def print_sorted(self):`
- **You can assume all elements are integers.**
- **No external modules allowed.**

**File:** `1-my_list.py`

### 2. Exact same object
**Description:**
Write a function `is_same_class` that returns `True` if the object is exactly an instance of the specified class, otherwise returns `False`.

- **Prototype:** `def is_same_class(obj, a_class):`
- **No external modules allowed.**

**File:** `2-is_same_class.py`

### 3. Same class or inherit from
**Description:**
Write a function `is_kind_of_class` that returns `True` if the object is an instance of, or inherited from, the specified class.

- **Prototype:** `def is_kind_of_class(obj, a_class):`
- **No external modules allowed.**

**File:** `3-is_kind_of_class.py`

### 4. Only sub class of
**Description:**
Write a function `inherits_from` that returns `True` if the object is an instance of a class that inherited from the specified class.

- **Prototype:** `def inherits_from(obj, a_class):`
- **No external modules allowed.**

**File:** `4-inherits_from.py`

### 5. Geometry module
**Description:**
Write an empty class `BaseGeometry`.

- **No external modules allowed.**

**File:** `5-base_geometry.py`

### 6. Improve Geometry
**Description:**
Write a class `BaseGeometry` with a method `area` that raises an exception with the message `area() is not implemented`.

- **Method:** `def area(self):`
- **No external modules allowed.**

**File:** `6-base_geometry.py`

### 7. Integer validator
**Description:**
Add a method `integer_validator` to the class `BaseGeometry` that validates if a value is an integer greater than 0.

- **Method:** `def integer_validator(self, name, value):`
- **Raises:** `TypeError` if the value is not an integer, `ValueError` if it's less than or equal to 0.
- **No external modules allowed.**

**File:** `7-base_geometry.py`

### 8. Rectangle
**Description:**
Create a class `Rectangle` that inherits from `BaseGeometry`. The class should have private attributes `width` and `height`, and the values must be validated using `integer_validator`.

- **Constructor:** `def __init__(self, width, height):`
- **No getters or setters allowed.**
- **No external modules allowed.**

**File:** `8-rectangle.py`

### 9. Full rectangle
**Description:**
Extend the `Rectangle` class to implement the `area` method and add a custom `__str__` method that prints `[Rectangle] <width>/<height>`.

- **Method:** `def area(self):`
- **No external modules allowed.**

**File:** `9-rectangle.py`

### 10. Square #1
**Description:**
Create a class `Square` that inherits from `Rectangle`. The `Square` class should implement the `area` method, and `size` must be validated.

- **Constructor:** `def __init__(self, size):`
- **No external modules allowed.**

**File:** `10-square.py`

### 11. Square #2
**Description:**
Extend the `Square` class to implement the custom `__str__` method that prints `[Square] <size>/<size>`.

- **Constructor:** `def __init__(self, size):`
- **No external modules allowed.**

**File:** `11-square.py`

## Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-inheritance`

