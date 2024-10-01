# Serialization Tasks

This repository contains a series of tasks focused on serialization techniques in Python. The tasks involve converting data between various formats such as JSON, CSV, and XML, as well as learning to handle custom objects using the `pickle` module.

## Tasks Overview

### 0. Basic Serialization
**Mandatory**

Create a basic serialization module to serialize a Python dictionary to a JSON file and deserialize it back to a dictionary.

- **Module**: `task_00_basic_serialization.py`
- **Functions**:
  - `serialize_and_save_to_file(data, filename)`: Serialize a Python dictionary and save it as a JSON file.
  - `load_and_deserialize(filename)`: Load and deserialize a JSON file back into a Python dictionary.

#### Example Usage:
```python
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data_to_serialize, 'data.json')
deserialized_data = load_and_deserialize('data.json')

## Task 1: Pickling Custom Classes

This task focuses on learning how to serialize and deserialize custom Python objects using the `pickle` module. You will create a custom class named `CustomObject` with attributes `name`, `age`, and `is_student`. The class will include a method to display its attributes, as well as methods for serialization and deserialization. The serialization method will save the object to a file, while the deserialization method will load the object from a file, handling any potential exceptions gracefully.

### Requirements
- Create a class `CustomObject` with the specified attributes.
- Implement `serialize` and `deserialize` methods.
- Handle exceptions for file operations.

## Task 2: Converting CSV Data to JSON Format

The objective of this task is to practice reading data from a CSV file and converting it into JSON format using serialization techniques. You will implement a function called `convert_csv_to_json`, which will take the name of a CSV file as input and write the corresponding JSON data to a file named `data.json`.

### Key Steps
- Import the necessary modules: `csv` and `json`.
- Use Python's `csv` module to read the data from the CSV file, converting each row into a dictionary with the `DictReader` class.
- Serialize the list of dictionaries into JSON format and save it to `data.json`.
- Return `True` if the conversion is successful; otherwise, return `False` if an exception occurs, such as file not found.

### Example CSV Dataset
The input CSV file (data.csv) should have the following format:


## Task 3: Serializing and Deserializing with XML

In this task, we will explore serialization and deserialization using XML as an alternative to JSON. You will implement two main functions: `serialize_to_xml` and `deserialize_from_xml`.

### Key Functions
- **serialize_to_xml(dictionary, filename)**: This function takes a Python dictionary and a filename as parameters. It serializes the dictionary into XML format and saves it to the specified filename.
  - Create a root element (e.g., `<data>`).
  - Iterate through the dictionary items and add them as child elements to the root.
  - Write the XML tree to the provided filename using the `xml.etree.ElementTree` module.

- **deserialize_from_xml(filename)**: This function takes a filename as its parameter, reads the XML data from that file, and reconstructs a Python dictionary from it.
  - Parse the XML file using `ET.parse`.
  - Navigate through the XML elements to rebuild the dictionary.
  - Be aware of data types, as XML does not differentiate between numbers and strings like Python.

