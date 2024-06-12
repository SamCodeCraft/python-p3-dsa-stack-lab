class Stack:

    def __init__(self, items = None, limit = 100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def empty(self):
        return len(self.items) == 0


    def push(self, value):
        if len(self.items) < self.limit:
            self.items.append(value)
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")


    def peek(self):
        if not self.empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit


    def search(self, target):
        try:
            index = self.items[::-1].index(target)
            return index
        except ValueError:
            return -1
