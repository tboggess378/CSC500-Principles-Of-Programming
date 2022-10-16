try:
    # Gets input from user for cost of each item
    item_price = float(input('Enter price for the first item: \n'))
    item_price2 = float(input('Enter price for the second item: \n'))
    item_price3 = float(input('Enter price for the third item: \n'))
    item_price4 = float(input('Enter price for the fourth item: \n'))
    item_price5 = float(input('Enter price for the fifth item: \n'))

    # Calculates subtotal of items and total with sales tax of 7%
    sub_total = item_price + item_price2 + item_price3 + item_price4 + item_price5
    sales_tax = 7
    total = sub_total * (sales_tax / 100)

    # Output statements to show item prices, subtotal, sales tax, and total
    print('RECEIPT')
    print(f'Item 1 price: {item_price:.2f}')
    print(f'Item 2 price: {item_price2:.2f}')
    print(f'Item 3 price: {item_price3:.2f}')
    print(f'Item 4 price: {item_price4:.2f}')
    print(f'Item 5 price: {item_price5:.2f}')
    print(f'Subtotal: {sub_total:.2f}')
    print(f'Sales tax: {sales_tax}%')
    print(f'Total: {total:.2f}')

# Displays error message when user enters any non number
except ValueError:
    print('Error. Invalid Entry.')
