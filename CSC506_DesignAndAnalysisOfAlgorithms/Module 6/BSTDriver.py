# Name: Tobias Boggess
# Date: July 23, 2023
# Purpose: The purpose is to build a binary tree that

from BinarySearchTree import BinarySearchTree


def main():
    input_option = int(input(f'Enter 1 for default array or 2 to input custom array: '))

    # gets the input from user to use default array or custom array
    while input_option not in [1, 2]:
        print(f'Please input a valid option.')
        input_option = int(input(f'Enter 1 for default array or 2 to input custom array: '))

    # prints a tree based on default array
    if input_option == 1:
        arr = [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]
        btree = BinarySearchTree(arr)

        print(f'Default Tree: ')
        print(btree)

    # allows user to enter singular values
    else:
        input_val = input(f'Enter value or \'exit\': ')
        btree = BinarySearchTree()
        while input_val != 'exit':
            btree.insert(int(input_val))
            input_val = input(f'Enter value or \'exit\': ')

        print(f'Custom Tree: ')
        print(btree)


if __name__ == '__main__':
    main()
