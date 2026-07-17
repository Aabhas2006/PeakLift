from user import User
from workout import Workout
from exercise import Exercise
from set import Set

print("=" * 34)
print("         🏋️ PeakLift")
print("=" * 34)
print("\nWelcome to PeakLift!")
print("\nLet's create your profile.\n")

name = input("Enter your name :")
age = input("Enter your age :")
gender = input("Enter your gender :")
height = input("Enter your height :")
weight = input("Enter your weight :")
goal = input("Enter your goal :")

user = User(name, age, gender, weight, height, goal)


print("\n✅ Profile created successfully!\n")
print(user)

print("\nLet's log today's workout!\n")

workout_date = input("Enter workout date: ")

workout = Workout(workout_date)

print("\nWorkout Created Successfully!\n")
print(workout)

print("\n Time to add exercises.\n")

exercise_name = input("Enter the exercise name: ")

exercise =  Exercise(exercise_name)

print("\nExercise created\n")
print(exercise)

workout.add_exercise(exercise)

print("\nExercise added to workout!\n")

print(workout)

number_of_sets = int(input("How many sets did you perform? "))

for i in range(number_of_sets):

    print(f"\nSet {i + 1}")

    weight = float(input("Weight (kg): "))
    reps = int(input("Reps: "))
    current_set = Set(reps, weight)
    exercise.add_set(current_set)

print("\nExercise Updated!\n")
print(exercise)

