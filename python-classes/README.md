# Holberton School - Python Classes

This repository contains tasks related to the creation and manipulation of Python classes, focusing on the implementation of a `Square` class.

## Table of Contents
- [Holberton School - Python Classes](#holberton-school---python-classes)
  - [Table of Contents](#table-of-contents)
  - [Task 0: My first square](#task-0-my-first-square)
  - [Task 1: Square with size](#task-1-square-with-size)
  - [Task 2: Size validation](#task-2-size-validation)
  - [Task 3: Area of a square](#task-3-area-of-a-square)
  - [Task 4: Access and update private attribute](#task-4-access-and-update-private-attribute)
  - [Task 5: Printing a square](#task-5-printing-a-square)
  - [Task 6: Coordinates of a square](#task-6-coordinates-of-a-square)
  - [Repository](#repository)

## Task 0: My first square
Write an empty class `Square` that defines a square:
- No module imports are allowed.

**File:** `0-square.py`

## Task 1: Square with size
Write a class `Square` that defines a square, adding:
- Private instance attribute `size`
- Class constructor that initializes `size`

**File:** `1-square.py`

## Task 2: Size validation
Enhance the `Square` class by adding:
- Validation of the `size` attribute: it must be an integer and >= 0, raising appropriate exceptions otherwise.

**File:** `2-square.py`

## Task 3: Area of a square
Extend the `Square` class with:
- A public instance method `area()` that returns the area of the square.

**File:** `3-square.py`

## Task 4: Access and update private attribute
Further improve the `Square` class by adding:
- Getter and setter methods for `size` to control access and validate the value.

**File:** `4-square.py`

## Task 5: Printing a square
Add a public instance method `my_print()` to the `Square` class that prints the square using the `#` character. If `size == 0`, it prints an empty line.

**File:** `5-square.py`

## Task 6: Coordinates of a square
Update the `Square` class to include:
- A `position` attribute (a tuple of two positive integers) that determines the square's indentation when printed.
- Modify the `my_print()` method to respect the `position` attribute when printing the square.

**File:** `6-square.py`

## Repository
- **GitHub repository:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool-higher_level_programming)
- **Directory:** `python-classes`
