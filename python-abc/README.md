# Python ABC and OOP Tasks

## 0. Abstract Animal Class and its Subclasses
**Objective**:
- Create an abstract class `Animal` using the `ABC` package with an abstract method `sound`.
- Implement two subclasses: `Dog` and `Cat` that inherit from `Animal` and define their own `sound` methods, returning "Bark" and "Meow" respectively.

**Key Concepts**:
- Abstract Base Classes (ABCs) ensure that derived classes implement specific methods.
- Use of the `@abstractmethod` decorator.

**Resources**:
- Python ABC documentation: [Python ABC](https://docs.python.org/3/library/abc.html)

---

## 1. Shapes, Interfaces, and Duck Typing
**Objective**:
- Create an abstract class `Shape` with two abstract methods: `area` and `perimeter`.
- Implement two concrete subclasses: `Circle` and `Rectangle`, both inheriting from `Shape`.
- Write a `shape_info` function that uses duck typing to accept any `Shape` object and print its area and perimeter.

**Key Concepts**:
- Duck typing: Object behavior is more important than the inheritance hierarchy.
- Abstract Base Classes (ABCs) and dynamic polymorphism.

**Resources**:
- [Concept of Duck Typing](https://realpython.com/lessons/duck-typing/)

---

## 2. Extending the Python List with Notifications
**Objective**:
- Create a `VerboseList` class that extends the Python `list` class.
- Override the `append`, `extend`, `remove`, and `pop` methods to print notifications when items are added or removed.

**Key Concepts**:
- Subclassing built-in classes to modify behavior.
- Use of the `super()` function to retain original functionality while adding custom behavior.

---

## 3. CountedIterator - Keeping Track of Iteration
**Objective**:
- Create a `CountedIterator` class that extends the built-in iterator and keeps track of how many items have been iterated over.
- Override the `__next__` method to increment a counter each time an item is fetched.

**Key Concepts**:
- Extending iterators in Python.
- Overriding the `__next__` method to enhance functionality.

---

## 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
**Objective**:
- Create a `FlyingFish` class that inherits from both `Fish` and `Bird` classes.
- Override the `fly`, `swim`, and `habitat` methods to customize behaviors of the flying fish.

**Key Concepts**:
- Multiple inheritance in Python.
- Method Resolution Order (MRO) and its importance in handling inherited methods.

---

## 5. The Mystical Dragon - Mastering Mixins
**Objective**:
- Design two mixin classes: `SwimMixin` and `FlyMixin` to add `swim` and `fly` methods.
- Create a `Dragon` class that inherits from both mixins and demonstrate that it can swim, fly, and roar.

**Key Concepts**:
- Mixins are used to add functionality to classes in a modular way.
- Mixin design should focus on specific, single behaviors to enhance code reusability.

---

**Repository**:
- **GitHub**: holbertonschool-higher_level_programming
- **Directory**: `python-abc`
