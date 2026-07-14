class User:

    def __init__(self, name, age, gender, weight, height, goal):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.goal = goal

    def update_weight(self, weight: float):
        
        self.weight = weight

    def update_goal(self, goal):

        self.goal = goal 
      

        

        
