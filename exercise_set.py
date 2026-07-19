class Set:

    def __init__(self , reps , weight):

        self.reps = reps
        self.weight = weight

    def update_reps(self, reps):
        self.reps = reps

    def  update_weight(self, weight):

        self.weight = weight

    def __str__(self):

        return f"{self.weight} kg × {self.reps} reps"

    def to_dict(self):

        return{
            "weight": self.weight,
            "reps": self.reps
        }