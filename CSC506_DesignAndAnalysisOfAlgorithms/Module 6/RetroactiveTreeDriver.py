# Name: Tobias Boggess
# Date: July 26, 2023
# Purpose: The purpose is to build a retroactive binary search trees

from PartialRetroactiveBST import PartialRetroactiveBST
from FullyRetroactiveBST import FullRetroactiveBST


def print_menu():
    print(f'1. Insert elements into tree in past or present')
    print(f'2. Delete elements from tree in past or present')
    print(f'3. Search for element from tree in past or present')
    print(f'4. Query tree')
    print(f'5. Exit program')


# Assume tree insertions are done at the start and in between deletions
def insert_operations(prbst, frbst):
    # Get value to input into the tree
    input_val = input(f'Enter value or \'exit\': ')
    time_ago = input(f'Enter past bst to search: ')
    while input_val != 'exit':
        prbst.insert_ago(int(input_val), int(time_ago))
        frbst.insert_ago(int(input_val), int(time_ago))
        input_val = input(f'Enter value or \'exit\': ')

        if input_val != 'exit':
            time_ago = input(f'Enter past bst to search: ')


# Assume insertions have already occurred in trees
def delete_operations(prbst, frbst):
    # Get value to delete from the tree and which tree to search
    input_val = input(f'Enter value to delete or \'exit\': ')
    time_ago = input(f'Enter past bst to search: ')
    while input_val != 'exit' and time_ago.isdigit():
        prbst.delete_ago(int(input_val), int(time_ago))
        frbst.delete_ago(int(input_val), int(time_ago))
        input_val = input(f'Enter value to delete or \'exit\': ')

        if input_val != 'exit':
            time_ago = input(f'Enter past bst to search: ')


# Search any iteration of each tree
def search_operations(prbst, frbst):
    # Get value to search from each tree and which iteration
    input_val = input(f'Enter value to delete or \'exit\': ')
    time_ago = input(f'Enter past bst to search: ')
    while input_val != 'exit' and time_ago.isdigit():
        print(f'{prbst.pred_ago(int(input_val), int(time_ago))}')
        print(f'{frbst.pred_ago(int(input_val), int(time_ago))}')
        input_val = input(f'Enter value to search or \'exit\': ')

        if input_val != 'exit':
            time_ago = input(f'Enter past bst to search: ')


# Print the tree from which to query. Only applicable to search previous tree iterations with
# Full Retroactive BST.
def query_operations(prbst, frbst):
    print(f'Custom PRBST Tree: ')
    print(f'Tree History: {prbst.tree_history}')
    prbst.query()

    which_tree = input(f'Enter a numeric option to query into previous tree: ')
    while not which_tree.isdigit() or 0 > int(which_tree) > 5:
        which_tree = input(f'Enter a numeric option ot query into previous tree: ')

    print(f'Custom FRBST Tree: ')
    print(f'Tree History: {frbst.tree_history}')
    frbst.query(int(which_tree))


def main():
    # Initialize trees to input values into
    prbst = PartialRetroactiveBST()
    frbst = FullRetroactiveBST()

    # Print Menu to select an option
    print_menu()
    menu_option = input(f'Enter option from menu: ')
    while menu_option.isdigit() and int(menu_option) in range(1, 6):
        menu_option = int(menu_option)
        if menu_option == 1:
            insert_operations(prbst, frbst)
        elif menu_option == 2:
            delete_operations(prbst, frbst)
        elif menu_option == 3:
            search_operations(prbst, frbst)
        elif menu_option == 4:
            query_operations(prbst, frbst)
        else:
            print(f'EXITING')
            break

        print_menu()
        menu_option = input(f'Enter option from menu: ')


if __name__ == '__main__':
    main()
