# Name: Tobias Boggess
# Date: 11-14-2022
# Purpose: Shopping cart to keep track of items to purchase

import re
from shopping_cart_item import ItemToPurchase


class ShoppingCart:
    # Constructor for Shopping Cart Class
    # Defaults: Customer Name: None
    #           Current Date: January 1, 2020
    #           Cart Items: Empty List
    def __init__(self, customer_name='none', current_date='January 1, 2020', cart_items=None):
        if cart_items is None:
            cart_items = []

        if len(customer_name) > 0:
            self.customer_name = customer_name.upper()
        else:
            self.customer_name = 'none'

        if len(current_date) > 0:
            self.current_date = current_date.upper()
        else:
            self.current_date = 'January 1, 2020'

        self.cart_items = cart_items

    # Gets customer name
    def get_customer_name(self):
        return self.customer_name

    # Gets current date
    def get_current_date(self):
        return self.current_date

    # Gets cart_items
    def get_cart_items(self):
        return self.cart_items

    # Sets customer name
    def set_customer_name(self, name):
        if len(name) > 0:
            self.customer_name = name.upper()
        else:
            self.customer_name = 'none'

    # Sets current date
    def set_current_date(self, date):
        if len(date) > 0:
            self.current_date = date
        else:
            self.current_date = 'January 1, 2020'

    # Sets cart_items list
    def set_cart_items(self, cart):
        if len(cart) > 0:
            self.cart_items.append(cart)
        else:
            self.cart_items = []

    # Inputs: item
    # Outputs: None
    # Purpose: Add item to cart
    def add_item(self, item):
        items = self.get_cart_items()
        found_in_cart = False

        # Updates quantity if item is already in list
        for i in range(len(items)):
            if items[i].item_name == item.item_name and \
                    items[i].item_price == item.item_price and \
                    items[i].item_description == item.item_description:
                found_in_cart = True
                print('Item found in cart please modify item quantity.\n')
                self.modify_item(item)
                break
        # Adds item to cart if similar item is not in cart already
        if not found_in_cart:
            self.cart_items.append(item)

    # Inputs: item_name (ItemToPurchase object)
    # Outputs: None
    # Purpose: Removes item from shopping cart
    def remove_item(self, item_name):
        try:
            # Store items and traverse item list
            items = self.get_cart_items()
            item_in_cart = False

            # Removes item from cart
            for i in range(len(items)):
                if items[i].item_name == item_name.item_name:
                    items.remove(items[i])
                    item_in_cart = True
                    break

            # If item is not in cart output no item found message
            if not item_in_cart:
                raise ValueError()

        # If item in cart is not found
        except ValueError:
            print('Item not found in cart. Nothing removed.')

    # Inputs: item (ItemToPurchase object)
    # Outputs: None
    # Purpose: Changes item's price, quantity, description based on item name
    def modify_item(self, item):
        try:
            # Gets index of cart item that matches the item given
            items = self.get_cart_items()
            idx = -1

            # Gets index for item in shopping cart that matches item given
            for i in range(len(items)):
                if items[i].item_name == item.item_name:
                    idx = i
                    break

            # Based on index, check the following
            if idx >= 0:
                # If default values, add item
                if (items[idx].item_price == 0.00) and \
                        (items[idx].item_quantity == 0) and \
                        (items[idx].item_description == ''):
                    print('Please update price, quantity, and description for item.')
                    try:
                        items[idx].set_item_price(float(input('Enter the item price: \n')))
                        items[idx].set_item_quantity(int(input('Enter the item quantity: \n')))
                    except ValueError:
                        print('Invalid character or price/quantity found.')
                        self.modify_item(item)
                    items[idx].set_item_description(input('Enter item description: \n'))

                # Update price, quantity, description given user input
                else:
                    try:
                        # items[idx].set_item_price(float(input('Enter item price: ')))
                        items[idx].item_quantity = int(input('Enter item quantity to purchase: '))
                    except ValueError:
                        print('Invalid character or invalid price/quantity.')
                    # items[idx].set_item_description(input('Enter item description: '))

            # If item is not found in shopping cart raise a value error
            else:
                raise ValueError
        # Tells user that no item was found and nothing was modified
        except ValueError:
            print('Item not found in cart. Nothing modified.')

    # Inputs: None
    # Outputs: total_items
    # Purpose: Finds the total number of items in the cart
    def get_num_items_in_cart(self):
        # Initializing total_items
        total_items = 0

        # Get quantities from cart items and update total_items
        for item in self.cart_items:
            total_items += item.get_item_quantity()
        return total_items

    # Inputs: None
    # Outputs: Returns total cost from item quantity and item price
    # Purpose: Calculates total cost
    def get_cost_of_cart(self):
        # Initialize total_cost
        total_cost = 0.00

        # Get total price from cart items
        for item in self.get_cart_items():
            total_cost += (item.get_item_quantity() * item.get_item_price())
        return total_cost

    # Inputs: None
    # Outputs: Returns a string (receipt) of shopping cart items
    # Purpose: Basic receipt for user
    def print_total(self):
        # Outputs Name of customer and the date supplied
        print(f'{self.get_customer_name()}\'s Shopping Cart - {self.get_current_date()}')

        # Checks if cart is empty
        if len(self.get_cart_items()) > 0:
            # Prints number of items in cart
            print(f'Number of items: {self.get_num_items_in_cart()}')

            # Prints price per item and quantity of each item
            for item in self.get_cart_items():
                item.print_item_cost()

            # Prints total cost from items in cart
            total_cost = self.get_cost_of_cart()
            print(f'Total Cost: ${total_cost:.2f}')
        else:
            print('SHOPPING CART IS EMPTY')

    # Inputs: None
    # Outputs: Returns a string with item descriptions
    # Purpose: Prints item descriptions to user
    def print_descriptions(self):
        # Prints customer name and current date
        print(f'{self.get_customer_name()}\'s Shopping Cart - {self.get_current_date()}')

        # Gets item descriptions and prints it to user
        if len(self.get_cart_items()) > 0:
            print(f'Item Descriptions')

            # Prints cart items with their respective descriptions
            for item in self.get_cart_items():
                print(f'{item.get_item_name()}: {item.get_item_description()}')
        else:
            print(f'SHOPPING CART IS EMPTY.')
