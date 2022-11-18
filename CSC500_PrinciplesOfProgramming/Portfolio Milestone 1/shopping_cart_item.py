# Name: Tobias Boggess
# Date: November 18, 2022
# Purpose: Creates a new ItemToPurchase object and adds the name, price,
# quantity, and description to a customers shopping cart


class ItemToPurchase:
    # Inputs: name, price, quantity
    # Defaults: name = none, price = 0.00, quantity = 0
    def __init__(self, item_name='none', item_price=0.00, item_quantity=0, item_description=''):
        self._item_name = item_name
        self._item_price = item_price
        self._item_quantity = item_quantity
        self._item_description = item_description

    # Gets item name
    @property
    def item_name(self):
        return self._item_name

    # Gets item price
    @property
    def item_price(self):
        return self._item_price

    # Gets item quantity
    @property
    def item_quantity(self):
        return self._item_quantity

    # Gets item description
    @property
    def item_description(self):
        return self._item_description

    # Sets item name
    @item_name.setter
    def item_name(self, name):
        if len(name) > 0:
            self._item_name = name
        else:
            self._item_name = 'none'

    # Sets item price
    @item_price.setter
    def item_price(self, price):
        try:
            if price > 0:
                self._item_price = price
            else:
                raise ValueError('Item price must be greater than 0.')
        except ValueError:
            print('Invalid character or item price found.')

    # Sets item quantity
    @item_quantity.setter
    def item_quantity(self, quantity):
        try:
            if quantity > 0:
                self._item_quantity = quantity
            else:
                raise ValueError('Item quantity must be greater than 0 to purchase.')
        except ValueError:
            print('Invalid quantity or character detected.')

    # Sets item description
    @item_description.setter
    def item_description(self, description):
        if len(description) > 0:
            self._item_description = description
        else:
            self._item_description = ''

    # Description: Prints total price per item based on quantity
    # Inputs: none
    # Outputs: String in format
    # item_name item_quantity @ item_price = item_total
    def print_item_cost(self):
        item_name = self._item_name
        item_price = self._item_price
        item_quantity = self._item_quantity
        total_cost = item_price * item_quantity

        print(f'{item_name} {item_quantity:.0f} @ ${item_price:.2f} = ${total_cost:.2f}')
