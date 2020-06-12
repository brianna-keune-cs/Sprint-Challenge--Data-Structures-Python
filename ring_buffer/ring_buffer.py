
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.count = 0

    def append(self, item):
        if len(self.storage) is self.capacity:
            if self.count == self.capacity:
                self.count = 0
            self.storage[self.count] = item
            self.count += 1
        else:
            self.storage.append(item)

    def get(self):
        return self.storage
