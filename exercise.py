from exercise_set import Set
class Exercise:

    def __init__(self, name):
        self.name = name
        self.sets = []

    def add_set(self, set):

         self.sets.append(set) 

    def remove_set(self, set):

        self.sets.remove(set)

    def __str__(self):

        text = f"Exercise: {self.name}\n"

        for index, set_obj in enumerate(self.sets, start=1):
            text += f"  Set {index}: {set_obj}\n"

        return text

    def to_dict(self):

        return {
            "exercise": self.name,
            "sets": [
                current_set.to_dict()
                for current_set in self.sets
            ]
        }

    @classmethod
    def from_dict(cls, data):

        exercise = cls(
            data["exercise"]
        )

        for set_data in data["sets"]:

            current_set = Set.from_dict(set_data)

            exercise.add_set(current_set)

        return exercise