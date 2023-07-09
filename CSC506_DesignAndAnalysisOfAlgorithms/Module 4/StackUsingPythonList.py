from ArrayList import ArrayList


class StackUsingPythonList:

    def __init__(self):
        self.stack = ArrayList()

    def push(self, data):
        self.stack.prepend(data)

    def pop(self):
        data = self.stack.array[0]
        self.stack.remove_at_idx(0)
        return data

    def peek(self):
        return self.stack.array[0]
