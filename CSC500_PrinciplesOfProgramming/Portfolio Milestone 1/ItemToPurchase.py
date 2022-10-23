class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.00, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    @property
    def item_name(self):
        return self.item_name

    @property
    def item_price(self):
        return self.item_price

    @property
    def item_quantity(self):
        return self.item_quantity

    @item_name.setter
    def item_name(self, item_name):
        if len(item_name) > 0:
            self.item_name = item_name
        else:
            self.item_name = 'none'

    @item_price.setter
    def item_price(self, item_price):
        if item_price > 0:
            self.item_price = item_price
        else:
            raise ValueError('Item price must be greater than 0.')

    @item_quantity.setter
    def item_quantity(self, item_quantity):
        if item_quantity > 0:
            self.item_quantity = item_quantity
        else:
            raise ValueError('Item quantity must be greater than 0 to purchase.')

    def print_item_cost(self):
        item_name = self.get_item_name()
        item_price = self.get_item_price()
        item_quantity = self.get_item_quantity()
        total_cost = item_price * item_quantity

        print('RECEIPT\n\n')
        print(f'{item_name} {item_quantity:.0f} @ ${item_price:.2f} = ${total_cost:.2f}')
