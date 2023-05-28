# Name: Tobias Boggess
# Date: May 28, 2023
# Purpose: Displays some of the steps in a stepwise diagram for a check writing program.

# Print the diagram in the following format
# First Step
# \tSecond Steps
# \t\t Third Step
# \t\t\t Fourth Step
def display_check_writing_diagram():
    print(f'Write a check')
    print(f'\tTake input for name')
    print(f'\tTake input for numerical dollar amount')
    print(f'\tTake input for written dollar amount')
    print(f'\tTake input for memo')
    print(f'\tTake input for signature')
    print(f'\t\tVerify Information for all categories')
    print(f'\t\t\tPrint the check')


def main():
    display_check_writing_diagram()


if __name__ == "__main__":
    main()
