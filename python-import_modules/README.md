# Python Import Modules Project

This project contains several Python scripts demonstrating the use of modules and import functions in Python.

## Tasks

### 0. Import a Simple Function
- **File:** `0-add.py`
- **Description:** This script imports the `add(a, b)` function from the `add_0.py` file and prints the result of adding two integers. The program outputs `1 + 2 = 3`.
- **Key Points:**
  - Uses the `print` function with string formatting to display integers.
  - Variables `a` and `b` are defined separately.
  - The import of `add_0` is done only once.

### 1. My First Toolbox!
- **File:** `1-calculation.py`
- **Description:** This script imports several functions from the `calculator_1.py` file (`add`, `sub`, `mul`, `div`), performs mathematical operations on the values `a = 10` and `b = 5`, and prints the results.
- **Key Points:**
  - Utilizes all four imported functions.
  - Variables `a` and `b` are used as arguments for each function.
  - The import of the module is done only once with `calculator_1`.

### 2. How to Make a Script Dynamic!
- **File:** `2-args.py`
- **Description:** This script prints the number of arguments passed to the program and lists them. It handles cases with no arguments, a single argument, or multiple arguments.
- **Key Points:**
  - Uses `argv` to retrieve the arguments.
  - Outputs the number of arguments and their values in a formatted manner.

### 3. Infinite Addition
- **File:** `3-infinite_add.py`
- **Description:** This script sums all the arguments passed via the command line and prints the result. It also works with very large numbers.
- **Key Points:**
  - Uses `int()` to convert arguments to integers.
  - The script handles the sum of multiple arguments.

### 4. Who Are You?
- **File:** `4-hidden_discovery.py`
- **Description:** This script prints all the names defined in the compiled module `hidden_4.pyc`, except for those that start with `__`.
- **Key Points:**
  - Names are printed one per line in alphabetical order.
  - The script ignores special names starting with `__`.

### 5. Everything Can Be Imported
- **File:** `5-variable_load.py`
- **Description:** This script imports a variable `a` from the file `variable_load_5.py` and prints its value.
- **Key Points:**
  - The script imports only the variable `a` without using `*` or `__import__`.
