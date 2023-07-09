class ArrayList:

    def __init__(self, initial_size = 10):
        self.list_size = initial_size
        self.length = 0
        self.array = [None] * initial_size

    def prepend(self, data):
        if self.list_size == self.length:
            self.resize(self.length * 2)

        for i in reversed(range(1, self.length+1)):
            self.array[i] = self.array[i-1]

        self.array[0] = data
        self.length += 1

    def append(self, data):
        if self.list_size == self.length:
            self.resize(self.length * 2)

        self.array[self.length] = data

        self.length += 1

    def insert_after(self, idx, data):
        if self.list_size == self.length:
            self.resize(self.length * 2)

        for i in reversed(range(idx+1, self.length+1)):
            self.array[i] = self.array[i-1]

        self.array[idx+1] = data

        self.length += 1

    def remove_at_idx(self, idx):
        if 0 <= idx < self.length:
            for i in range(idx, self.length-1):
                self.array[i] = self.array[i+1]

            self.length -= 1

    def search(self, data):
        for i in range(self.length):

            if self.array[i] == data:
                return data

        return -1

    def resize(self, new_list_size):
        new_array = [None] * new_list_size

        for i in range(self.length):
            new_array[i] = self.array[i]

        self.array = new_array

        self.list_size = new_list_size
