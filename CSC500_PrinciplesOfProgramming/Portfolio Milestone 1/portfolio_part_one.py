# Name: Tobias Boggess
# Date: November 18, 2022,
# Purpose: From a menu, a user can choose an option to add an item, change
# an item, remove an item, or output a receipt, or output descriptions of the
# items in the shopping cart.


from shopping_cart import *
from shopping_cart import *


# Description: Finds total cost of items in a shopping cart
# Inputs: Object list containing items
# Outputs: cost per item, total cost
def find_total_cost(shopping_cart):
    total_cost = 0.00

    for item in shopping_cart:
        total_cost += (item.item_price * item.item_quantity)
        item.print_item_cost()

    print(f'Total: ${total_cost:.2f}')


# Shows a menu for user to add an item, remove an item,
# change an item (price, quantity, description),
# print outputs of item descriptions, print receipt for all items,
# and exit out of the program
def print_menu(cart):
    while True:
        # Menu to Choose an option from
        print(f'MENU')
        print(f'a - Add item to cart')
        print(f'r - Remove item from cart')
        print(f'c - Change item quantity')
        print(f'i - Output items\' descriptions')
        print(f'o - Output shopping cart')
        print(f'q - Quit')
        choice = input('Choose an option: ')

        if choice == 'a':
            item = input('\nEnter item name: \n')
            price = float(input('Enter the item price: \n'))
            quantity = int(input('Enter the item quantity: \n'))
            description = input('Enter item description: \n')
            cart.add_item(ItemToPurchase(item, price, quantity, description))
            print()
        elif choice == 'r':
            item = ItemToPurchase(input('\nWhat item would you like removed: '))
            cart.remove_item(item)
            print()
        elif choice == 'c':
            item = ItemToPurchase(input('\nChange quantity for what item: '))
            cart.modify_item(item)
            print()
        elif choice == 'i':
            print(f'\nOUTPUT ITEMS\' DESCRIPTIONS')
            cart.print_descriptions()
            print()
        elif choice == 'o':
            print(f'\nOUTPUT SHOPPING CART')
            cart.print_total()
            print()
        elif choice == 'q':
            print(f'\nQUITING')
            break
        else:
            print('\nMust be a character described in menu.')
            print()


def main():
    # Shopping cart to contain all items to purchase
    name = input('Enter name: ')
    date = input('Enter date: ')
    cart = ShoppingCart(name, date)
    print_menu(cart)


if __name__ == '__main__':
    main()
