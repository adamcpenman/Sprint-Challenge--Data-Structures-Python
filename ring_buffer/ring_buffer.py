class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_data = 0

    def append(self, item):
        # check length of list is less than capacity
        if len(self.storage) < self.capacity:
            # append item to the list
            self.storage.append(item)
        # if list reached capacity
        else:
            # append item by replacing item at oldest index
            self.storage[self.oldest_data] = item
            # check oldest item is the last item
            if self.oldest_data < len(self.storage) - 1:
                # if not increment oldest index
                self.oldest_data += 1
            else:
                # reset oldest to first index
                self.oldest_data = 0

    def get(self):
        return self.storage
