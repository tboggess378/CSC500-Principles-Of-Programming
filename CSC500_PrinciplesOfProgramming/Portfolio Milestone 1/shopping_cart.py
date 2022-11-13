# Name: Tobias Boggess
# Date: 11-14-2022
# Purpose:

from shopping_cart_item import ItemToPurchase


class ShoppingCart:
    def __init__(self, customer_name=None, current_date='January 1, 2020', cart_items=[]):
        self._customer_name = customer_name
        self._current_date = current_date
        self._cart_items = cart_items

    @property
    def customer_name(self):
        return self._customer_name

    @property
    def current_date(self):
        return self._current_date

    @property
    def cart_items(self):
        return self._cart_items

    @customer_name.setter
    def customer_name(self, customer_name):
        self._customer_name = customer_name

    @current_date.setter
    def current_date(self, current_date):
        self._current_date = current_date

    @cart_items.setter
    def cart_items(self, cart_items):
        self._cart_items = cart_items

    def add_item(self, item):
        if item in self._cart_items:
            self.modify_item(item)
        else:
            self._cart_items.append(item)

    def remove_item(self, item_name):
        try:
            self._cart_items.remove(item_name)
        except ValueError:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, item):
        try:
            items = self._cart_items[:]
            item_names = []
            for i in range(len(items)):
                item_names.append(items[i].item_name)

            if item in item_names:
                if(item.item_price == 0.00) and \
                        (item.item_quantity == 0) and \
                        (item.item_description == ''):
                    return
                else:
                    item.item_price = float(input('Enter item price: '))
                    item.item_quantity = int(input('Enter item quantity to purchase: '))
                    item.item_description = input('Enter item description: ')
            else:
                raise ValueError
        except ValueError:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        total_items = 0
        for item in self._cart_items:
            total_items += item.item_quantity
        return total_items

    def get_cost_of_cart(self):
        total_cost = 0.00
        for item in self._cart_items:
            total_cost += (item.item_quantity * item.item_price)
        return total_cost

    def print_total(self):
        print(f'{self._customer_name}\'s Shopping Cart - {self._current_date}')
        if len(self._cart_items) > 0:
            print(f'Number of items: {self.get_num_items_in_cart()}')
            for item in self._cart_items:
                item.print_item_cost()
            total_cost = self.get_cost_of_cart()
            print(f'Total Cost: ${total_cost:.2f}')
        else:
            print('SHOPPING CART IS EMPTY')

    def print_descriptions(self):
        print(f'{self._customer_name}\'s Shopping Cart - {self._current_date}')
        if len(self._cart_items) > 0:
            print(f'Item Descriptions')
            for item in self._cart_items:
                print(f'{item.item_name}: {item.item_description}')


