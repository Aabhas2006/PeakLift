from user import User
from workout import Workout
from exercise import Exercise
from exercise_set import Set

user = User.load()

if user:

    print(f"\nWelcome back, {user.name}! 👋")

else:

    print("\nWelcome to PeakLift!")
    print("\nLet's create your profile.\n")

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    height = input("Enter your height (cm): ")
    weight = input("Enter your weight (kg): ")
    goal = input("Enter your goal: ")

    user = User(name, age, gender, weight, height, goal)

    user.save()

    print("\n✅ Profile created successfully!\n")


print("\n" + "=" * 40)
print("        🏋️ PeakLift Menu")
print("=" * 40)

print("1. Log New Workout")
print("2. View Workout History")
print("3. View Profile")
print("4. Exit")

choice = input("\nChoose an option: ")


if choice == "1":

    print("\nLet's log today's workout!\n")

    workout_date = input("Enter workout date: ")

    workout = Workout(workout_date)

    another_exercise = "Y"

    while another_exercise == "Y":

        print("\n----------------------------")
        print("Add New Exercise")
        print("----------------------------")

        exercise_name = input("Exercise Name: ")

        exercise = Exercise(exercise_name)

        number_of_sets = int(input("How many sets did you perform? "))

        for i in range(number_of_sets):

            print(f"\nSet {i + 1}")

            weight = float(input("Weight (kg): "))
            reps = int(input("Reps: "))

            current_set = Set(reps, weight)

            exercise.add_set(current_set)

        workout.add_exercise(exercise)

        another_exercise = input(
            "\nDo you want to add another exercise? (Y/N): "
        ).upper()

    user.add_workout(workout)

    user.save()

    print("\n" + "=" * 40)
    print("        WORKOUT SUMMARY")
    print("=" * 40)

    print(user)

    print("\n" + "=" * 40)
    print(" Thank you for using PeakLift! 💪")
    print("=" * 40)


elif choice == "2":

    print("\n========== WORKOUT HISTORY ==========\n")

    for workout in user.workouts:
        print(workout)


elif choice == "3":

    print("\n========== PROFILE ==========\n")
    print(user)


elif choice == "4":

    print("\nThank you for using PeakLift! 💪")


else:

    print("\nInvalid option!")