class Workout:

    def __init__(self, date):

        self.date = date
        self.exercises = [] 

    def add_exericse(self, exercise):

        self.exercises.append(exercise)

    def remove_exercise(self, exercise):

        self.exercises.remove(exercise)