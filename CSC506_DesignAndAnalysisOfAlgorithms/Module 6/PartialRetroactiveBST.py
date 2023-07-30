# Name: Tobias Boggess
# Date: July 24, 2023
# Purpose: Creates a partially retroactive search tree to insert nodes, delete nodes
# querying the present tree,

from BinarySearchTree import BinarySearchTree
from Node import Node
import warnings
import copy


class PartialRetroactiveBST:
    # Constructor
    def __init__(self, data=[]):
        self.bst = BinarySearchTree(data)
        self.tree_history = [None] * 15
        self.tree_history[0] = self.bst
        self.latest_tree = 0

    # Used to insert values into a binary tree past or present
    def insert_ago(self, data, time_ago=0):
        # See when to insert the value into a previous tree
        if time_ago >= len(self.tree_history) - 1 or self.tree_history[self.latest_tree - time_ago] is None:

            while time_ago > len(self.tree_history) - 1:
                warnings.warn(f'Insert a valid tree to insert into.')
                time_ago = input(f'Enter a numerical value for a previous version of the BST or \'exit\''
                                 f'(i.e., Time_ago = 2 will insert into the binary tree 2 iterations ago.): ')

                if time_ago == 'exit':
                    print(f'Cancelling insertion.')
                    return
                else:
                    time_ago = int(time_ago)
                    break

        # Update the latest tree only if the time ago is in the present
        if time_ago == 0 and self.latest_tree < len(self.tree_history):
            self.latest_tree += 1
        elif self.latest_tree >= len(self.tree_history) - 1:
            time_ago = self.remove_tree_copy()
            self.latest_tree += 1

        # Get a copy of the tree from time_ago
        past_bst = copy.deepcopy(self.tree_history[self.latest_tree - time_ago - 1])
        past_bst.insert(Node(data))
        self.tree_history[self.latest_tree] = past_bst

        # update next trees to include the values inserted
        if time_ago != 0:
            for idx in range(self.latest_tree - time_ago + 1, self.latest_tree):
                current_tree = copy.deepcopy(self.tree_history[idx])
                current_tree.insert(Node(data))
                self.tree_history[idx] = current_tree

    # Delete a value from a tree past/present
    def delete_ago(self, data, time_ago=0):
        # Check for valid time
        if time_ago >= len(self.tree_history) - 1 or self.tree_history[self.latest_tree - time_ago] is None:

            while time_ago > len(self.tree_history) - 1:
                warnings.warn(f'Insert a valid tree to delete from.')
                time_ago = input(f'Enter a numerical value for a previous version of the BST or \'exit\''
                                 f'(i.e., Time_ago = 2 will insert into the binary tree 2 iterations ago.): ')

                if time_ago == 'exit':
                    print(f'Cancelling deletion.')
                    return
                else:
                    time_ago = int(time_ago)
                    break

        # Update latest_tree
        if time_ago == 0 and self.latest_tree < len(self.tree_history) and self.latest_tree != 0:
            self.latest_tree += 1
        elif self.latest_tree >= len(self.tree_history) - 1:
            time_ago = self.remove_tree_copy()
            self.latest_tree += 1

        # get a copy to insert in the tree history
        past_bst = copy.deepcopy(self.tree_history[self.latest_tree - time_ago - 1])
        past_bst.remove_key(data)
        self.tree_history[self.latest_tree] = past_bst

        # continue the process for next trees
        if time_ago != 0:
            for idx in range(self.latest_tree - time_ago + 1, self.latest_tree):
                current_tree = copy.deepcopy(self.tree_history[idx])
                current_tree.remove_key(data)
                self.tree_history[idx] = current_tree

    # Searches a binary tree past/present
    def pred_ago(self, data, time_ago=0):
        # Determine if previous tree exists
        if time_ago >= len(self.tree_history) - 1 or self.tree_history[self.latest_tree - time_ago] is None:

            while time_ago > len(self.tree_history) - 1:
                warnings.warn(f'Insert a valid tree to delete from.')
                time_ago = input(f'Enter a numerical value for a previous version of the BST or \'exit\''
                                 f'(i.e., Time_ago = 2 will insert into the binary tree 2 iterations ago.): ')

                if time_ago == 'exit':
                    print(f'Cancelling deletion.')
                    return
                else:
                    time_ago = int(time_ago)
                    break

        # Make a deep copy of tree from time_ago
        past_bst = copy.deepcopy(self.tree_history[self.latest_tree - time_ago])
        current = past_bst.root

        found_value = past_bst.search(data)
        if found_value is not None:
            return found_value.key

        # Search the tree and return largest next value if not found
        while current is not None:
            if current.key == data:
                return current.key
            elif current.key > data:
                if current.left is not None and current.left.key > data:
                    current = current.left
                else:
                    return current.key
            else:
                if current.right is not None and current.right.key < data:
                    current = current.right
                else:
                    return current.key

        return None

    # Updates the history to limit the amount of memory taken
    def remove_tree_copy(self, time_ago):
        # Delete the trees in the first five locations as these are the oldest
        for i in range(5):
            self.tree_history[i] = None

        # Move trees into the removed trees above
        k = 0
        for j in range(5, self.latest_tree):
            self.tree_history[k] = self.tree_history[j]
            k += 1

        # update lastest_tree and time_ago
        self.latest_tree = self.latest_tree - 5
        time_ago += 5
        return time_ago

    # Print the present tree
    def query(self):
        print(f'{print(self.tree_history[self.latest_tree])}')
