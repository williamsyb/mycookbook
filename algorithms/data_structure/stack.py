class Stack:
    def __init__(self, size_limit=None):
        self.__size_limit = size_limit
        self.elements = []
        self.__size = 0

    def push(self, value):
        if self.__size_limit is not None and len(self.elements) > self.__size_limit:
            raise IndexError('Stack is full')
        else:
            self.elements.append(value)
            self.__size += 1

    def is_empty(self):
        return self.__size == 0

    def clear(self):
        self.elements = []
        self.__size = 0

    def size(self):
        return self.__size

    def top(self):
        return self.elements[-1]

    def pop(self):
        val = self.elements.pop()
        self.__size -= 1
        return val
