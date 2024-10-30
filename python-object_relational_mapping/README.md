### Task Summary for README

This repository contains scripts and files for managing and interacting with a MySQL database using Python. The tasks involve various operations such as listing states, filtering states by name, handling SQL injections, and using SQLAlchemy for Object-Relational Mapping (ORM).

#### Tasks Overview:

1. **Get all states**
   - Script: `0-select_states.py`
   - Description: Lists all states from the database `hbtn_0e_0_usa`.
   - Arguments: MySQL username, password, and database name.
   - Uses: `MySQLdb` module.
   - Results: Sorted by `states.id` in ascending order.

2. **Filter states**
   - Script: `1-filter_states.py`
   - Description: Lists all states with names starting with 'N' from the database `hbtn_0e_0_usa`.
   - Arguments: MySQL username, password, and database name.
   - Uses: `MySQLdb` module.
   - Results: Sorted by `states.id` in ascending order.

3. **Filter states by user input**
   - Script: `2-my_filter_states.py`
   - Description: Lists all states where the name matches the user input from the database `hbtn_0e_0_usa`.
   - Arguments: MySQL username, password, database name, and state name.
   - Uses: `MySQLdb` module.
   - Results: Sorted by `states.id` in ascending order.

4. **SQL Injection**
   - Script: `3-my_safe_filter_states.py`
   - Description: Lists all states where the name matches the user input, safe from SQL injections.
   - Arguments: MySQL username, password, database name, and state name.
   - Uses: `MySQLdb` module.
   - Results: Sorted by `states.id` in ascending order.

5. **Cities by states**
   - Script: `4-cities_by_state.py`
   - Description: Lists all cities from the database `hbtn_0e_4_usa`.
   - Arguments: MySQL username, password, and database name.
   - Uses: `MySQLdb` module.
   - Results: Sorted by `cities.id` in ascending order.

6. **All cities by state**
   - Script: `5-filter_cities.py`
   - Description: Lists all cities of a given state from the database `hbtn_0e_4_usa`.
   - Arguments: MySQL username, password, database name, and state name.
   - Uses: `MySQLdb` module.
   - Results: Sorted by `cities.id` in ascending order.

7. **First state model**
   - Script: `model_state.py`
   - Description: Defines the `State` class using SQLAlchemy.
   - Arguments: MySQL username, password, and database name.
   - Uses: `SQLAlchemy` module.
   - Results: Creates the `states` table in the database.

8. **All states via SQLAlchemy**
   - Script: `7-model_state_fetch_all.py`
   - Description: Lists all `State` objects from the database `hbtn_0e_6_usa`.
   - Arguments: MySQL username, password, and database name.
   - Uses: `SQLAlchemy` module.
   - Results: Sorted by `states.id` in ascending order.

9. **First state**
   - Script: `8-model_state_fetch_first.py`
   - Description: Prints the first `State` object from the database `hbtn_0e_6_usa`.
   - Arguments: MySQL username, password, and database name.
   - Uses: `SQLAlchemy` module.
   - Results: Displays the first state in `states.id`.

10. **Contains `a`**
    - Script: `9-model_state_filter_a.py`
    - Description: Lists all `State` objects containing the letter 'a' from the database `hbtn_0e_6_usa`.
    - Arguments: MySQL username, password, and database name.
    - Uses: `SQLAlchemy` module.
    - Results: Sorted by `states.id` in ascending order.

11. **Get a state**
    - Script: `10-model_state_my_get.py`
    - Description: Prints the `State` object with the name passed as an argument from the database `hbtn_0e_6_usa`.
    - Arguments: MySQL username, password, database name, and state name.
    - Uses: `SQLAlchemy` module.
    - Results: Displays the `states.id` or "Not found" if no match.

12. **Add a new state**
    - Script: `11-model_state_insert.py`
    - Description: Adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`.
    - Arguments: MySQL username, password, and database name.
    - Uses: `SQLAlchemy` module.
    - Results: Prints the new `states.id` after creation.

13. **Update a state**
    - Script: `12-model_state_update_id_2.py`
    - Description: Changes the name of the `State` object where `id = 2` to "New Mexico" in the database `hbtn_0e_6_usa`.
    - Arguments: MySQL username, password, and database name.
    - Uses: `SQLAlchemy` module.
    - Results: Updates the state name in the database.

14. **Delete states**
    - Script: `13-model_state_delete_a.py`
    - Description: Deletes all `State` objects with names containing the letter 'a' from the database `hbtn_0e_6_usa`.
    - Arguments: MySQL username, password, and database name.
    - Uses: `SQLAlchemy` module.
    - Results: Deletes the specified states from the database.

15. **Cities in state**
    - Script: `model_city.py`, `14-model_city_fetch_by_state.py`
    - Description: Defines the `City` class and lists all `City` objects from the database `hbtn_0e_14_usa`.
    - Arguments: MySQL username, password, and database name.
    - Uses: `SQLAlchemy` module.
    - Results: Displays cities grouped by their states.

#### Repository Structure:
- **GitHub repository**: `holbertonschool-higher_level_programming`
- **Directory**: `python-object_relational_mapping`
- **Files**:
  - `0-select_states.py`
  - `1-filter_states.py`
  - `2-my_filter_states.py`
  - `3-my_safe_filter_states.py`
  - `4-cities_by_state.py`
  - `5-filter_cities.py`
  - `model_state.py`
  - `7-model_state_fetch_all.py`
  - `8-model_state_fetch_first.py`
  - `9-model_state_filter_a.py`
  - `10-model_state_my_get.py`
  - `11-model_state_insert.py`
  - `12-model_state_update_id_2.py`
  - `13-model_state_delete_a.py`
  - `model_city.py`
  - `14-model_city_fetch_by_state.py`

This summary provides an overview of the tasks and their corresponding scripts, along with the repository structure.
