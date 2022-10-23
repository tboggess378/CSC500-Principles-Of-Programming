import ItemToPurchase


def find_total_cost(shopping_cart):
    total_cost = 0.00

    for item in shopping_cart:
        total_cost += item.price
        item.print_item_cost()

    print(f'Total: ${total_cost:.2f}')


def main():
    shopping_cart = []

    for i in range(2):
        print(f'Item {i}')
        item = input('Enter item name: \n')
        price = input('Enter the item price: \n')
        quantity = input('Enter the item quantity: \n')
        shopping_cart.append(ItemToPurchase(item, price, quantity))


if __name__ == '__main__':
    main()
