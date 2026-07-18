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