class Queue:
    def __init__(self ,max = 100):
        self.list=[None]* max
        self.front = -1
        self.rear = -1
    def insert(self,x):
        if self.rear >= len(self.list) -1 :
            print("Queue is Full")
            return
        if  self.front == -1 :
            self.front+= 1 
            self.rear+= 1
            self.list[list.rear] = x
            return
        self.rear+= 1 
        self.list[self.rear] = x
    def Del(self):
        if self.front == -1 :
            print("Queue is empty")
            return     
        if  self.front == self.rear :
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        k = self.list[self.front]
        self.front+= 1
        return k
    
test = Queue(3)
test.insert(57)
test.insert(32)
test.insert(44)
test.insert(39) 
test.Del()
test.insert(39) 





class C_Queue:
    def __init__(self, max):
        self.list = [] * max
        self.front = -1
        self.rear = -1
    def  insert(self , x):
        if (self.rear +1) % len(self.list) == self.front:
            print("Queue is full")
            return
        if  self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[0] = x
            return
        self.rear=(self.rear +1) % len(self.list)
        self.list[self.rear] = x
    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return
        if self.front == self.rear:
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        k = self.list[self.front]
        self.front = (self.front +1) % len (self.list)
        return k
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear +1) % len (self.list) == self.front