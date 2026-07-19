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