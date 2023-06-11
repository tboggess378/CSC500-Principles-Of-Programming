# Name: Tobias Boggess
# Date: June 11, 2023
# Purpose: Outline the steps for a state condition for an ATM machine.
# This is a preliminary python script to tell the available steps.
# May not reflect the actual implementation for the ATM.

# Prints steps from start to finish of successful completion of ATM usage
def print_steps():
    # Beginning of transaction between customer.
    # Check for pin and bank information to see compatibility
    # On unsuccessful PIN enters. Increases counter until a certain value is hit and exits to main menu
    # and eats the card.
    # On successful PIN entry. Continues to next GUI
    print(f'ATM Machine')
    print(f'Enter account information (card and pin)')
    print(f'Send message to server. Check banking information.')
    print(f'Continue to customer information and take in PIN.')
    print(f'Send message to server. Check the PIN and increase counter if PIN is incorrect.')
    print(f'\tOn successful PIN entry. Ask for user selected option.')
    print(f'\tOn unsuccessful PIN entry and counter is above allowable. Exit to main menu.')

    # Options available to customer
    # Allow for multiple account transactions as long as withdraw cash is not selected.
    # Ask if user has any other transactions they would like to make.
    # Check if balance is 0 or below. Close account if balance hits 0 or below.
    print(f'OPTIONS:')
    print(f'\tDeposit Money')
    print(f'\tView Account Balance')
    print(f'\tGet Cash')
    print(f'\t\tCheck account balance')
    print(f'\t\t\tClose account if balance is 0 or less')
    print(f'\tMake a balance transfer')
    print(f'\t\tCheck account balance')
    print(f'\t\t\tClose account if balance is 0 or less')
    print(f'\tGo back to options if previously selected was not withdraw cash')
    print(f'\tExit to main menu otherwise. Return card after transaction')

    # Return card regardless of account closure. Exit to main menu for another transaction.
    print(f'Return card after transaction(s). Exit to main menu')


# Execution of program
def main():
    print_steps()


# Runs the program
if __name__ == "__main__":
    main()
