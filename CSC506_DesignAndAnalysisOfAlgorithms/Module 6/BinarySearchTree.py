# Name: Tobias Boggess
# Date: July 22, 2023
# Purpose: Binary tree to store data into

from TreePrint import pretty_tree
from Node import Node


# sort the data in place using gnome sort
def gnome_sort(data):
    n = len(data)
    index = 0

    # traverse through the array
    while index < n:

        # increase the index if start of the array or if value is greater than previous
        if index == 0:
            index += 1
        if data[index] >= data[index - 1]:
            index += 1

        # swap values in array and decrease index
        else:
            data[index], data[index - 1] = data[index - 1], data[index]
            index -= 1


# removes duplicates from input array
def remove_duplicates(data):
    arr = []

    # only add values to array if no duplicates exist
    for val_idx in range(len(data)):
        if data[val_idx] not in arr:
            arr.append(data[val_idx])

    return arr


# builds a tree from a given input array
def build_tree(data):
    # initialize a binary tree, sort the array, remove duplicates
    btree = BinarySearchTree()
    gnome_sort(data)
    data = remove_duplicates(data)

    # insert unique values into tree
    for val in data:
        btree.insert(Node(val))

    return btree.root


class BinarySearchTree:
    # constructor for binary tree
    def __init__(self, data=[]):
        self.data = data

        # set root to empty if no data is input
        if len(data) == 0:
            self.root = None

        # add values in array to tree after sorting
        else:
            self.root = build_tree(data)

    # inserts a new value into the tree
    def insert(self, node):

        # check for root
        if self.root is None:
            self.root = node
            node.parent = None

        # root exists
        else:
            current_node = self.root
            while current_node is not None:

                # determine if value should be added to the left child
                if node.key < current_node.key:
                    if current_node.left is None:
                        current_node.left = node
                        node.parent = current_node
                        current_node = None
                    else:
                        current_node = current_node.left

                # determine if value should be added to the right child
                elif node.key > current_node.key:
                    if current_node.right is None:
                        current_node.right = node
                        node.parent = current_node
                        current_node = None
                    else:
                        current_node = current_node.right

                # don't add value if it exists already
                else:
                    print(f'Value already exists in tree.')
                    break

            # re-balance tree from child nodes to the root
            node = node.parent
            while node is not None:
                self.rebalance(node)
                node = node.parent

    # re-balance the tree
    def rebalance(self, node):
        # update heights for input node
        node.update_height()

        # determine if a right rotation then left rotation is needed
        if node.get_balance() == -2:
            if node.right.get_balance() == 1:
                self.rotate_right(node.right)

            return self.rotate_left(node)

        # determine if a left rotation then right rotation is needed
        elif node.get_balance() == 2:
            if node.left.get_balance() == -1:
                self.rotate_left(node.left)

            return self.rotate_right(node)

        return node

    # search for a given node in the tree
    def search(self, key):
        # start at the root, iterate through child leafs
        current_node = self.root
        while current_node is not None:
            if current_node.key == key:
                return current_node
            elif current_node.key < key:
                current_node = current_node.right
            else:
                current_node = current_node.left

    # remove a node from the tree
    def remove_key(self, key):
        node = self.search(key)
        if node is None:
            return False
        else:
            return self.remove_node(node)

    # removes a node from the tree based on key
    def remove_node(self, node):
        if node is None:
            return False

        # get the parent node of the input node
        parent = node.parent

        # case when there is a left child and a right child
        if node.left is not None and node.right is not None:
            successor_node = node.right
            while successor_node.left is not None:
                successor_node = successor_node.left

            node.key = successor_node.key
            self.remove_node(successor_node)

            return True

        # case when the node is the root
        elif node is self.root:
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right

            if self.root is not None:
                self.root.parent = None

            return True

        # case when there is a left child
        elif node.left is not None:
            parent.replace_child(node, node.left)

        # case when there is a right child
        else:
            parent.replace_child(node, node.right)

        # rebalance the tree starting from subtrees
        node = parent
        while node is not None:
            self.rebalance(node)
            node = node.parent

        return True

    # rotates subtrees based on balance weights of nodes
    def rotate_left(self, node):
        right_left_child = node.right.left

        # replaces parent with right node and place parent as left node
        if node.parent is not None:
            node.parent.replace_child(node, node.right)

        # set the root as the right node and the parent node to none
        else:
            self.root = node.right
            self.root.parent = None

        # set right and left child of node
        node.right.set_child('l', node)
        node.set_child('r', right_left_child)

        return node.parent

    # rotates subtrees based on balance weights of nodes
    def rotate_right(self, node):
        left_right_child = node.left.right

        # place parent node as right child and left child as parent node
        if node.parent is not None:
            node.parent.replace_child(node, node.left)

        # place left child as root
        else:
            self.root = node.left
            self.root.parent = None

        # set left and right children
        node.left.set_child('r', node)
        node.set_child('l', left_right_child)

        return node.parent

    # prints string of tree copyright is part of TreePrint
    def __str__(self):
        return pretty_tree(self)
