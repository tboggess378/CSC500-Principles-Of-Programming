# Name: Tobias Boggess
# Date: November 7, 2022,
# Purpose: Simple program to decide the number of points someone
# earns during a month of purchasing book.

def main():
    try:
        # asks user to enter the number of book purchased this month
        books_purchased = int(input('Enter the number of books purchased: '))
        points = 0

        # award points based on number of book purchased
        if books_purchased >= 0:
            if books_purchased >= 8:
                points = 60
            elif books_purchased >= 6:
                points = 30
            elif books_purchased >= 4:
                points = 15
            elif books_purchased >= 2:
                points = 5
            else:
                points = 0
        else:
            raise ValueError()

        # prints how many points are awarded based on user input
        print(f'Points awarded this month: {points}')
    except ValueError:
        print('Non-integer or negative was entered.')


if __name__ == '__main__':
    main()
