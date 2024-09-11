# Python Test-Driven Development Tasks

## 0. Integers Addition
- **Objective**: Write a function that adds 2 integers.
- **Function Prototype**: `def add_integer(a, b=98):`
- **Details**:
  - `a` and `b` must be integers or floats.
  - If not, raise a `TypeError` with appropriate messages.
  - Convert floats to integers before addition.
  - The function returns the sum of `a` and `b`.
  - No modules allowed.

## 1. Divide a Matrix
- **Objective**: Write a function that divides all elements of a matrix.
- **Function Prototype**: `def matrix_divided(matrix, div):`
- **Details**:
  - `matrix` must be a list of lists of integers or floats.
  - All rows in `matrix` must have the same size.
  - `div` must be a number and cannot be 0.
  - The function returns a new matrix with all elements divided by `div`, rounded to 2 decimal places.
  - No modules allowed.

## 2. Say My Name
- **Objective**: Write a function that prints "My name is `<first name>` `<last name>`".
- **Function Prototype**: `def say_my_name(first_name, last_name=""):`
- **Details**:
  - `first_name` and `last_name` must be strings.
  - Raise a `TypeError` if they are not.
  - No modules allowed.

## 3. Print Square
- **Objective**: Write a function that prints a square with the character `#`.
- **Function Prototype**: `def print_square(size):`
- **Details**:
  - `size` must be an integer.
  - Raise a `TypeError` if it is not an integer.
  - If `size` is less than 0, raise a `ValueError`.
  - No modules allowed.

## 4. Text Indentation
- **Objective**: Write a function that prints a text with 2 new lines after each of these characters: `.`, `?`, and `:`.
- **Function Prototype**: `def text_indentation(text):`
- **Details**:
  - `text` must be a string.
  - Raise a `TypeError` if it is not a string.
  - No space should be at the beginning or end of each printed line.
  - No modules allowed.

## 5. Max Integer - Unittest
- **Objective**: Write unittests for the function `def max_integer(list=[])`.
- **Details**:
  - Tests should be written in a separate file inside a `tests` folder.
  - Use the `unittest` module.
  - All edge cases should be covered.

## Repository
- **GitHub Repository**: `holbertonschool-higher_level_programming`
- **Directory**: `python-test_driven_development`
