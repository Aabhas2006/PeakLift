class Workout:

    def __init__(self, date):

        self.date = date
        self.exercises = [] 

    def add_exercise(self, exercise):

        self.exercises.append(exercise)

    def remove_exercise(self, exercise):

        self.exercises.remove(exercise)

    def __str__(self):

        text = f"Workout Date: {self.date}\n\n"

        for exercise in self.exercises:
            text += f"{exercise}\n"

        return text