# Tasks

## 0. Squared Simple

**Mandatory**

Write a function that computes the square value of all integers in a matrix.

- **Prototype:** `def square_matrix_simple(matrix=[]):`
- **Requirements:**
  - `matrix` is a 2-dimensional array.
  - Returns a new matrix of the same size with each value being the square of the input value.
  - Initial matrix should not be modified.
  - No module imports allowed. Regular loops, map, etc. are permitted.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 0-square_matrix_simple.py

## 1. Search and Replace

**Mandatory**

Write a function that replaces all occurrences of an element with another in a new list.

- **Prototype:** `def search_replace(my_list, search, replace):`
- **Requirements:**
  - `my_list` is the initial list.
  - `search` is the element to replace.
  - `replace` is the new element.
  - No module imports allowed.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 1-search_replace.py

## 2. Unique Addition

**Mandatory**

Write a function that adds all unique integers in a list (only once for each integer).

- **Prototype:** `def uniq_add(my_list=[]):`
- **Requirements:**
  - No module imports allowed.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 2-uniq_add.py

## 3. Present in Both

**Mandatory**

Write a function that returns a set of common elements in two sets.

- **Prototype:** `def common_elements(set_1, set_2):`
- **Requirements:**
  - No module imports allowed.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 3-common_elements.py

## 4. Only Differents

**Mandatory**

Write a function that returns a set of all elements present in only one set.

- **Prototype:** `def only_diff_elements(set_1, set_2):`
- **Requirements:**
  - No module imports allowed.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 4-only_diff_elements.py

## 5. Number of Keys

**Mandatory**

Write a function that returns the number of keys in a dictionary.

- **Prototype:** `def number_keys(a_dictionary):`
- **Requirements:**
  - No module imports allowed.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 5-number_keys.py

## 6. Print Sorted Dictionary

**Mandatory**

Write a function that prints a dictionary by ordered keys.

- **Prototype:** `def print_sorted_dictionary(a_dictionary):`
- **Requirements:**
  - All keys are strings.
  - Keys should be sorted alphabetically.
  - Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary).
  - Dictionary values can have any type.
  - No module imports allowed.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 6-print_sorted_dictionary.py

## 7. Update Dictionary

**Mandatory**

Write a function that replaces or adds a key/value in a dictionary.

- **Prototype:** `def update_dictionary(a_dictionary, key, value):`
- **Requirements:**
  - `key` argument will always be a string.
  - `value` argument can be of any type.
  - If a key exists, the value will be replaced. If not, the key will be created.
  - No module imports allowed.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 7-update_dictionary.py

## 8. Simple Delete by Key

**Mandatory**

Write a function that deletes a key in a dictionary.

- **Prototype:** `def simple_delete(a_dictionary, key=""):`
- **Requirements:**
  - `key` argument will always be a string.
  - If a key doesn’t exist, the dictionary won’t change.
  - No module imports allowed.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 8-simple_delete.py

## 9. Multiply by 2

**Mandatory**

Write a function that returns a new dictionary with all values multiplied by 2.

- **Prototype:** `def multiply_by_2(a_dictionary):`
- **Requirements:**
  - Assume all values are integers.
  - Returns a new dictionary.
  - No module imports allowed.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 9-multiply_by_2.py

## 10. Best Score

**Mandatory**

Write a function that returns the key with the biggest integer value.

- **Prototype:** `def best_score(a_dictionary):`
- **Requirements:**
  - Assume all values are integers.
  - If no score found, return `None`.
  - Assume all students have a different score.
  - No module imports allowed.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 10-best_score.py

## 11. Multiply by Using Map

**Mandatory**

Write a function that returns a list with all values multiplied by a number without using any loops.

- **Prototype:** `def multiply_list_map(my_list=[], number=0):`
- **Requirements:**
  - Returns a new list of the same length as `my_list`, with each value multiplied by `number`.
  - Initial list should not be modified.
  - No module imports allowed.
  - Use `map`.
  - File should be a maximum of 3 lines.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 11-multiply_list_map.py

## 12. Roman to Integer

**Mandatory**

Technical interview preparation: Create a function that converts a Roman numeral to an integer.

- **Prototype:** `def roman_to_int(roman_string):`
- **Requirements:**
  - Number will be between 1 to 3999.
  - Return an integer.
  - If `roman_string` is not a string or is `None`, return 0.
  - No module imports allowed.

**Repository:**
- **GitHub:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** python-more_data_structures
- **File:** 12-roman_to_int.py
