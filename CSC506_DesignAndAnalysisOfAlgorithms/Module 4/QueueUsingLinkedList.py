from Node import Node
from DoublyLinkedList import DoublyLinkedList


class QueueUsingLinkedList:

    def __init__(self):
        self.queue = DoublyLinkedList()

    def push(self, data):
        self.queue.append(Node(data))

    def pop(self):
        data = self.queue.head.data
        self.queue.remove(self.queue.head)
        return data

    def peek(self):
        return self.queue.head.data
