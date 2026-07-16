class Exercise:

    def __init__(self, name):
        self.name = name
        self.sets = []

    def add_set(self, set):

         self.sets.append(set) 

    def remove_set(self, set):

        self.sets.remove(set)
