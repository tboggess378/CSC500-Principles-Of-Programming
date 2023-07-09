from ArrayList import ArrayList


class QueueUsingPythonList:

    def __init__(self):
        self.queue = ArrayList()

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        data = self.queue.array[0]
        self.queue.remove_at_idx(0)
        return data

    def peek(self):
        return self.queue.array[0]
