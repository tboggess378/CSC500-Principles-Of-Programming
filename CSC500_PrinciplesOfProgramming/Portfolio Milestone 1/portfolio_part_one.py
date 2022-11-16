from shopping_cart_item import *
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


def print_menu(cart):
    while True:
        print(f'MENU')
        print(f'a - Add item to cart')
        print(f'r - Remove item from cart')
        print(f'c - Change item quantity')
        print(f'i - Output items\' descriptions')
        print(f'o - Output shopping cart')
        print(f'q - Quit')
        choice = input('Choose an option: ')

        if choice == 'a':
            item = input('Enter item name: \n')
            price = float(input('Enter the item price: \n'))
            quantity = int(input('Enter the item quantity: \n'))
            description = input('Enter item description: \n')
            cart.add_item(ItemToPurchase(item, price, quantity, description))
        elif choice == 'r':
            item = ItemToPurchase(input('What item would you like removed: '))
            cart.remove_item(item)
        elif choice == 'c':
            item = ItemToPurchase(input('Change quantity for what item: '))
            cart.modify_item(item)
        elif choice == 'i':
            print(f'OUTPUT ITEMS\' DESCRIPTIONS')
            cart.print_descriptions()
        elif choice == 'o':
            print(f'OUTPUT SHOPPING CART')
            cart.print_total()
        elif choice == 'q':
            print(f'QUITING')
            break
        else:
            print('Must be a character described in menu.')


def main():
    # Shopping cart to contain all items to purchase
    name = input('Enter name: ')
    date = input('Enter date: ')
    cart = ShoppingCart(name, date)
    print_menu(cart)


if __name__ == '__main__':
    main()
