# Name: Tobias Boggess
# Date: May 7, 2023
# Purpose: Shows the screens available in the mobile app for the shopping lists
# and the general flow between the pages.


# Display options for which page to continue to
def displayPages():
    print(f'1: Shopping List Page')
    print(f'2: Shopping Cart Page')
    print(f'3: Payment Page and Store Locator Page')
    print(f'4: User Profile and Settings Page')
    print(f'5: Exit\n')


# Displays the current page based on user input
def displayCurrentPage(option):

    # Display the following options, exit on any option other than 1-4
    if option == 1:
        print(f'Shopping List')
        print(f'\tCreate List')
        print(f'\tModify List')
        print(f'\tDelete List\n')
    elif option == 2:
        print(f'Shopping Cart')
        print(f'\tAdd Item')
        print(f'\tRemove Item')
        print(f'\tModify Quantity of Items\n')
    elif option == 3:
        print(f'Payment Screen')
        print(f'\tContinue to checkout')
        print(f'\tYes or No')
        print(f'\tStore Locator')
        print(f'\t\tPayment Information to order items\n')
    elif option == 4:
        print(f'User Profile and Settings')
        print(f'\tUser Profile Settings')
        print(f'\t\tSettings options')
        print(f'\tChange Password')
        print(f'\t\tEnter Current Password')
        print(f'\t\tEnter new password')
        print(f'\t\tEnter new password again')
        print(f'\tChange Location')
        print(f'\t\tEnter new location')
        print(f'\tChange Darkmode')
        print(f'\t\tChange from darkmode to lightmode or vice versa')
        print(f'\tPrivacy and User Agreements')
        print(f'\t\tPrint of Privacy and User Agreements\n')
    elif option == 5:
        print(f'Exiting. Closing the App.')
    else:
        print(f'Exiting. Invalid Option.')


# Returns the number of pages in the mobile app
def showNumPages():
    return 4


# Executes program
def main():

    # Display the total number of pages available
    print(f'Number of Pages: {showNumPages()}')

    # Can transition dynamically between pages so only exits once user want to
    while True:
        # Display the screen options for the mobile app
        displayPages()

        # Get user input on which screen they would like to move to
        screen_option = int(input(f'Please input numerical numbers (1-4) to switch from one page to the other: '))
        displayCurrentPage(screen_option)

        # Want to stop execution if exit option is chosen or invalid option
        if screen_option not in [1, 2, 3, 4]:
            break


if __name__ == "__main__":
    main()
