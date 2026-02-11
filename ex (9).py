class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def prioritize(self):
        temp = []
        while not self.is_empty():
            temp.append(self.pop())

        temp.sort(reverse=True)

        for x in temp:
            self.push(x)