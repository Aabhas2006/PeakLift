# DAY-03

## What I have built?
- Created user class.
- Add methods to update weight and height.

## What I learned
- The user class should not have input() or print()
- Methods should update the object's state
- Parameters are values passed into methods
- self.attribute stores the object's current state

## Challenges
- Converting logic into code
- Understanding self.weight vs weight

## Tomorrow
- Design and implement the Workout class

----------------------------------------------------------------

# Day 4

## ✅ What I Built

* Designed and implemented the `Workout` class.
* Added support for storing multiple exercises using a list.
* Implemented `add_exercise()` and `remove_exercise()` methods.

## 🧠 What I Learned

* A `Workout` contains multiple `Exercise` objects, so using a list is the right approach.
* Constructors should only include information available when an object is created.
* Learned the difference between `append()`, `remove()`, and `pop()`.
* Designing the class before writing code makes implementation much easier.

## 💡 Challenges

* Deciding what belongs in the constructor.
* Understanding when to use `remove()` instead of `pop()`.

## 🎯 Next Step

* Design and implement the `Exercise` class.
* Continue building the relationship between `Workout`, `Exercise`, and `Set`.

## Day 4

### ✅ What I Built

* Implemented the `Workout` class.
* Added support for storing multiple exercises using a list.
* Implemented `add_exercise()` and `remove_exercise()` methods.
* Designed and implemented the `Exercise` class.
* Designed and implemented the `Set` class.

### 🧠 What I Learned

* A `Workout` contains multiple `Exercise` objects.
* An `Exercise` contains multiple `Set` objects.
* A `Set` stores only `weight` and `reps`.
* Understood the difference between `remove()` and `pop()`.
* Learned that designing classes before coding leads to cleaner architecture.

### 💡 Challenges

* Deciding what each class should own.
* Understanding object relationships (Workout → Exercise → Set).

### 🎯 Next Step

* Connect all classes together.
* Start implementing JSON storage for persistent workout data.
