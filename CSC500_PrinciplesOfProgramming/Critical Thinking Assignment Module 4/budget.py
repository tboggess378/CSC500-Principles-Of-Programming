# Name: Tobias Boggess
# Date: October 30, 2022
# Purpose: Asks users to enter expenses for a month
import math


def main():
    budget = 0.00
    user_input = ''
    expenses = []
    total_expenses = 0.00

    try:
        # User enters budget for expenses
        budget = float(input('Enter budget for month: '))
        while budget < 0:
            budget = float(input('Budget must be greater than zero. Enter budget for month: '))

        # Get expenses for the month
        user_input = input('Enter expense amount or (\'q\', \'Q\', \'quit\', \'Quit\') to exit: ')
        while (user_input not in ['q', 'Q', 'quit', 'Quit']) or (float(user_input) > 0.00):
            expenses.append(float(user_input))
            total_expenses += float(user_input)
            user_input = input('Enter expense amount or (\'q\', \'Q\', \'quit\', \'Quit\') to exit: ')
            if user_input in ['q', 'Q', 'quit', 'Quit']:
                break

        # Print output of total expenses, over or under budget, and by how much
        print(f'Total expenses: ${total_expenses:.2f}')
        print(f'Budget for month: ${budget:.2f}')

        if (budget - total_expenses) < 0:
            print(f'Over budget by: ${math.fabs(budget - total_expenses):.2f}')
        else:
            print(f'Under budget by: ${(budget - total_expenses):.2f}')
    except ValueError:
        print('Invalid character entered.')


if __name__ == '__main__':
    main()
