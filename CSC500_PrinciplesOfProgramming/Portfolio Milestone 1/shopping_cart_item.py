# Name: Tobias Boggess
# Date: November 18, 2022
# Purpose: Creates a new ItemToPurchase object and adds the name, price,
# quantity, and description to a customers shopping cart


class ItemToPurchase:
    # Inputs: name, price, quantity
    # Defaults: name = none, price = 0.00, quantity = 0
    def __init__(self, item_name='none', item_price=0.00, item_quantity=0, item_description=''):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Gets item name
    def get_item_name(self):
        return self.item_name

    # Gets item price
    def get_item_price(self):
        return self.item_price

    # Gets item quantity
    def get_item_quantity(self):
        return self.item_quantity

    # Gets item description
    def get_item_description(self):
        return self.item_description

    # Sets item name
    def set_item_name(self, name):
        if len(name) > 0:
            self.item_name = name
        else:
            self.item_name = 'none'

    # Sets item price
    def set_item_price(self, price):
        try:
            if len(price) > 0:
                if float(price) > 0:
                    self.item_price = float(price)
                elif float(price) == 0:
                    self.item_price = 0
                    self.set_item_quantity('0')
                    print('Quantity set to 0 since price is 0.')
                else:
                    raise ValueError()
            else:
                raise ValueError()
        except ValueError:
            print('Invalid character or item price found.')
            price = input('Enter a valid price: ')
            self.set_item_price(price)

    # Sets item quantity
    def set_item_quantity(self, quantity):
        try:
            if len(quantity) > 0:
                if self.get_item_price() > 0:
                    self.item_quantity = int(quantity)
                else:
                    self.item_quantity = 0
            else:
                raise ValueError()
        except ValueError:
            print('Invalid quantity or character detected.')
            quantity = input('Enter a valid quantity: ')
            self.set_item_quantity(quantity)

    # Sets item description
    def set_item_description(self, description):
        if len(description) > 0:
            self.item_description = description
        else:
            self.item_description = ''

    # Description: Prints total price per item based on quantity
    # Inputs: none
    # Outputs: String in format
    # item_name item_quantity @ item_price = item_total
    def print_item_cost(self):
        item_name = self.get_item_name()
        item_price = self.get_item_price()
        item_quantity = self.get_item_quantity()
        total_cost = item_price * item_quantity

        print(f'{item_name} {item_quantity:.0f} @ ${item_price:.2f} = ${total_cost:.2f}')
