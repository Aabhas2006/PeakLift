import json
class User:

    def __init__(self, name, age, gender, weight, height, goal):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.goal = goal
        self.workouts = []

    def update_weight(self, weight: float):
        
        self.weight = weight

    def update_goal(self, goal):

        self.goal = goal

    def add_workout(self, workout):

        self.workouts.append(workout)

    def remove_workout(self, workout):

        self.workouts.remove(workout) 

    def __str__(self):

        text = (
            f"========== User ==========\n"
            f"Name   : {self.name}\n"
            f"Age    : {self.age}\n"
            f"Gender : {self.gender}\n"
            f"Height : {self.height} cm\n"
            f"Weight : {self.weight} kg\n"
            f"Goal   : {self.goal}\n\n"
        )

        for workout in self.workouts:
            text += f"{workout}\n"

        return text

    def to_dict(self):

        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "goal": self.goal,
            "workouts": [
                workout.to_dict()
                for workout in self.workouts
            ]  
        }

    def save(self):

        with open("data/users.json", "w") as file:
            json.dump(self.to_dict(), file, indent=4)