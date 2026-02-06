class stack : 
    def __init__(self , limit = 1000):
        self.st=[]
        self.lim = limit
    def push(self , x):
        if len(self.st) >= self.lim:
           print("stack is full")
           return -1
        self.st.append(x)
    def pop(self):
        if len(self.st) == 0 :
            print("stack is empty")
            return -1
        return self.st.pop()
    def peek(self):
        if len(self.st) == 0 :
            print("stack is empty")
            return -1
        return self.st[-1]

test = stack(10)
test.push(57)
test.push(126)
test.push(-10)
k=test.peek()

def find(self,x):
    for i in range(len(self.st)):
        if self.st[i] == x :
           print(i)

def find1(self,x):
    for i in range(len(self.st)):
        if self.st[i] == x :
           print(i)
           return

def find2(self,x):
    for i in range(len(self.st)-1,-1,-1) :
        if self.st[i] == x :
            print(i)
            return
def find2_n(self,x):
    for i in range(len(self.st)):
        if self.st[i] == x :
            p=i
    print(p)

def find2_n(self,x):
    list=[]
    for i in range(len(self.st)):
        if self.st[i] == x :
            list.append(i)
    print(list[2])

def replace(self,x,y):
    for i in range(len(self.st)):
        if self.st[i] == x :
            self.st[i]=y