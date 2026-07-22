from exercise import Exercise
class Workout:

    def __init__(self, date):

        self.date = date
        self.exercises = [] 

    def add_exercise(self, exercise):

        self.exercises.append(exercise)

    def remove_exercise(self, exercise):

        self.exercises.remove(exercise)

    def __str__(self):

        text = f"========== Workout ==========\n"
        text += f"Date : {self.date}\n\n"

        for exercise in self.exercises:
            text += f"{exercise}\n"

        return text

    def to_dict(self):

        return {
            "date": self.date,
            "exercises": [
                exercise.to_dict()
                for exercise in self.exercises
            ]
        }

    @classmethod
    def from_dict(cls, data):

        workout = cls(
            data["date"]
        )

        for exercise_data in data["exercises"]:

            current_exercise = Exercise.from_dict(exercise_data)

            workout.add_exercise(current_exercise)

        return workout