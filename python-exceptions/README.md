# Python Exceptions Tasks

## 0. Safe List Printing
- **Function:** `safe_print_list(my_list=[], x=0)`
- **Description:** Prints `x` elements from `my_list`.
- **Notes:**
  - `my_list` can contain any data type.
  - Prints elements on the same line.
  - Returns the actual number of elements printed.
  - Must handle exceptions with `try`/`except`.
  - No modules or `len()` function allowed.

## 1. Safe Printing of an Integers List
- **Function:** `safe_print_integer(value)`
- **Description:** Prints an integer using `"{:d}".format()`.
- **Notes:**
  - Returns `True` if the value is correctly printed as an integer.
  - Returns `False` otherwise.
  - Must handle exceptions with `try`/`except`.
  - No modules or `type()` function allowed.

## 2. Print and Count Integers
- **Function:** `safe_print_list_integers(my_list=[], x=0)`
- **Description:** Prints the first `x` elements of `my_list` that are integers.
- **Notes:**
  - Only integers are printed; other types are skipped.
  - Returns the number of integers printed.
  - Must handle exceptions with `try`/`except`.
  - No modules or `len()` function allowed.

## 3. Integers Division with Debug
- **Function:** `safe_print_division(a, b)`
- **Description:** Divides two integers and prints the result.
- **Notes:**
  - The result is printed in the `finally:` section preceded by `Inside result:`.
  - Returns the division result or `None` if an error occurs.
  - Must handle exceptions with `try`/`except`/`finally`.

## 4. Divide a List
- **Function:** `list_division(my_list_1, my_list_2, list_length)`
- **Description:** Divides elements of two lists element by element.
- **Notes:**
  - Returns a new list containing the results of the divisions.
  - Handles exceptions such as division by zero, type errors, and out-of-range errors with specific error messages.
  - Must handle exceptions with `try`/`except`/`finally`.
  - No modules allowed.

## 5. Raise Exception
- **Function:** `raise_exception()`
- **Description:** Raises a `TypeError`.
- **Notes:**
  - No modules allowed.

## 6. Raise a Message
- **Function:** `raise_exception_msg(message="")`
- **Description:** Raises a `NameError` with a custom message.
- **Notes:**
  - No modules allowed.
