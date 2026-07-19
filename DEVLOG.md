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

## Day-05

### What I Learned

* Took user input using `input()`.
* Created `User`, `Workout`, `Exercise`, and `Set` objects dynamically from user input.
* Connected objects using OOP composition (`User → Workout → Exercise → Set`).
* Used loops to create multiple sets based on user input.
* Improved my understanding of constructors and object creation.
* Learned how `__str__()` allows objects to display themselves in a readable format.
* Practiced debugging common Python errors like `TypeError` and `AttributeError`.

### Progress

* PeakLift is now an interactive console application instead of using hardcoded data.
* Users can create a profile, log a workout, add an exercise, and enter sets through the terminal.

### Next Goal

* Allow users to add multiple exercises to a workout.
* Improve the overall application flow.
* Save workout data using JSON so it persists after closing the program.

## Day-06: Added Multiple Exercise Support

### What I Learned

* Learned when to use a `while` loop instead of a `for` loop.
* Implemented a sentinel-controlled loop to allow users to add multiple exercises.
* Improved my understanding of application flow in `main.py`.
* Practiced organizing code into logical sections for better readability.
* Connected multiple `Exercise` objects to a single `Workout` object.
* Improved the overall console user experience with a cleaner workflow.

### Progress

* Users can now log multiple exercises within a single workout.
* Each exercise can contain multiple sets with their own weight and reps.
* Refactored `main.py` to make the application flow cleaner and easier to maintain.
* PeakLift can now record a complete workout instead of being limited to a single exercise.

### Next Goal

* Create and manage a weekly workout plan.
* Save user and workout data using JSON.
* Allow users to view their workout history.

# Day-07

## What I Learned

* Learned object serialization using `to_dict()`.
* Implemented JSON saving with Python's `json` module.
* Added `to_dict()` methods to all classes.
* Understood why only the `User` class should handle saving.

## Progress

* Created a `data/` folder and `user.json`.
* Successfully saved complete workout data (User → Workout → Exercise → Set).
* Refactored `main.py` by moving saving logic into `user.save()`.

## Next Goal

* Load existing user data from `user.json`.
* Welcome returning users instead of creating a new profile every time.
