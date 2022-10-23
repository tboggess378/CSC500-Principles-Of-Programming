from ItemToPurchase import *

# Description: Finds total cost of items in a shopping cart
# Inputs: Object list containing items
# Outputs: cost per item, total cost
def find_total_cost(shopping_cart):
    total_cost = 0.00

    for item in shopping_cart:
        total_cost += (item.item_price * item.item_quantity)
        item.print_item_cost()

    print(f'Total: ${total_cost:.2f}')


def main():
    # Shopping cart to contain all items to purchase
    shopping_cart = []

    # Takes input from user for each item, price, and quantity
    # Stores item objects to a list
    for i in range(2):
        print(f'Item {i + 1}')
        item = input('Enter item name: \n')
        price = float(input('Enter the item price: \n'))
        quantity = int(input('Enter the item quantity: \n'))
        shopping_cart.append(ItemToPurchase(item, price, quantity))

    # prints the receipt
    # Contains cost per single item, total cost per item,
    # total costs for all items
    print('\nRECEIPT')
    find_total_cost(shopping_cart)


if __name__ == '__main__':
    main()
