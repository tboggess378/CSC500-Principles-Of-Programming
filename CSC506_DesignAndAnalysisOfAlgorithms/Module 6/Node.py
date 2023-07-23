# Name: Tobias Boggess
# Date: July 22, 2023
# Purpose: Nodes to be used in binary trees.

class Node:
    # constructor
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.right = None
        self.left = None
        self.height = 0

    # determines the balance of the (sub)trees
    def get_balance(self):
        left_height = -1
        right_height = -1

        if self.left is not None:
            left_height = self.left.height

        if self.right is not None:
            right_height = self.right.height

        return left_height - right_height

    # updates the height of the (sub)tree(s)
    def update_height(self):
        left_height = -1
        right_height = -1

        if self.left is not None:
            left_height = self.left.height

        if self.right is not None:
            right_height = self.right.height

        self.height = max(left_height, right_height) + 1

    # sets the children based on balancing factor of subtree
    def set_child(self, which_child, child):
        if which_child != 'l' and which_child != 'r':
            return False

        if which_child == 'l':
            self.left = child
        else:
            self.right = child

        if child is not None:
            child.parent = self

        self.update_height()
        return True

    # replaces children of parent
    def replace_child(self, current_child, new_child):
        if self.left is current_child:
            return self.set_child('l', new_child)
        elif self.right is current_child:
            return self.set_child('r', new_child)

        return False
