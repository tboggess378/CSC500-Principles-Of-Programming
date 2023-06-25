import sys, operator, random
from nutrition import Food, MealPlan

# Constants to be used by the greedy algorithm.
NUTRIENT_THRESHOLD = 0.001
FRACTION_THRESHOLD = 0.05
CALORIE_THRESHOLD = 0.1
MAX_CALORIES = 2000


def load_nutrient_data(filename):
    # Open file, read food items one line at a time,
    # create Food objects and append them to a list.
    # Return the list once the entire file is processed.
    food_items = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(',')
            line = line.split(':')
            food_items.append(Food(line[0], line[1], line[2], line[3], line[4]))
    return food_items


def sort_food_list(foods, nutrient):
    # Sort the food list based on the percent-by-calories of the
    # given nutrient ('protein', 'carbs' or 'fat')
    # The list is sorted in-place; nothing is returned.
    pass


def create_meal_plan(foods, nutrient, goal):
    # A greedy algorithm to create a meal plan that has MAX_CALORIES
    # calories and the goal amount of the nutrient (e.g. 30% protein)
    plan = MealPlan()
    return plan


def print_menu():
    print()
    print("\t1 - Set maximum protein")
    print("\t2 - Set maximum carbohydrates")
    print("\t3 - Set maximum fat")
    print("\t4 - Exit program")
    print()


if __name__ == "__main__":
    # 1. Load the food data from the file (change this to a user
    # prompt for the filename)
    filename = "food_data_small.txt"
    # filename = input(f'Enter name of food data file: ', end = '')
    print()
    foods = load_nutrient_data(filename)
    print(foods)

    # 2. Display menu and get user's choice. Repeat menu until a
    # valid choice is entered by the user (1-4, inclusive).
    print_menu()
    user_choice = int(input(f'Enter choice (1-4): ', end=''))
    print()
    while user_choice not in range(1, 5):
        print_menu()
        user_choice = int(input(f'Enter choice (1-4): ', end=''))
    # 3. Prompt user for goal nutrient percent value. Repeat prompt
    # until a valid choice is entered by the user (0-100, inclusive)
    percent_of_ingredient = -1.0
    while True:
        if user_choice == 1:
            percent_of_ingredient = int(input(f'What percentage of calories from protein is the goal? ', end=''))

        elif user_choice == 2:
            percent_of_ingredient = int(input(f'What percentage of calories from carbs is the goal? ', end=''))

        elif user_choice == 3:
            percent_of_ingredient = int(input(f'What percentage of calories from fat is the goal? ', end=''))

        elif user_choice == 4:
            break

        if 0.0 <= percent_of_ingredient <= 100.0:
            break
        else:
            continue
    # 4. Run greedy algorithm to create the meal plan.
    plan = createMealPlan(foods, nutrient, goal)

    # 5. Display plan.
    print(plan)