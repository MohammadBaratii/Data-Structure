class Queue:
    def __init__(self, size=10):
        self.size = size
        self.arr = [None] * size
        self.front = 0
        self.rear = -1

    def enqueue(self, x):
        if self.rear == self.size - 1:
            print("Queue Overflow")
            return
        self.rear += 1
        self.arr[self.rear] = x

    def dequeue(self):
        if self.front > self.rear:
            print("Queue Underflow")
            return
        self.front += 1

    def fix_queue(self):
        j = 0
        for i in range(self.front, self.rear + 1):
            self.arr[j] = self.arr[i]
            j += 1

        self.rear = self.rear - self.front
        self.front = 0

    def display(self):
        if self.front > self.rear:
            print("Queue is empty")
            return
        for i in range(self.front, self.rear + 1):
            print(self.arr[i], end=" ")
        print()