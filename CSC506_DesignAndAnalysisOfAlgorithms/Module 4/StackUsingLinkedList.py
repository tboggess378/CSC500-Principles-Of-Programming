from DoublyLinkedList import DoublyLinkedList
from Node import Node


class StackUsingLinkedList:

    def __init__(self):
        self.linked_list = DoublyLinkedList()

    def push(self, data):
        new_node = Node(data)
        self.linked_list.prepend(new_node)

    def pop(self):
        data = self.linked_list.head.data

        self.linked_list.remove(None)

        return data

    def peek(self):
        return self.linked_list.head.data

    def isEmpty(self):
        if self.linked_list.head is None:
            return True
        else:
            return False

    def getSize(self):
        if self.linked_list.head is None:
            return 0
        else:
            current_node = self.linked_list.head
            size = 0

            while current_node.next is not None:
                size += 1

            return size
