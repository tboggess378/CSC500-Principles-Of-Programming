from DoublyLinkedList import DoublyLinkedList
from Node import Node


class StackUsingLinkedList:

    def __init__(self):
        self.stack = DoublyLinkedList()

    def push(self, data):
        self.stack.prepend(Node(data))

    def pop(self):
        data = self.stack.head.data
        self.stack.remove(self.stack.head)
        return data

    def peek(self):
        return self.stack.head.data
