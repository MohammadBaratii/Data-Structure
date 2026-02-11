import random

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class doublelinklist:
    def __init__(self, capa):
        self.head = None
        self.tail = None
        self.s = 0
        self.capasity = capa

    def insert_after(self, node_data, new_data):
        cur = self.head
        while cur:
            if cur.data == node_data:
                new_node = Node(new_data)
                new_node.prev = cur
                new_node.next = cur.next
                if cur.next:
                    cur.next.prev = new_node
                else:
                    self.tail = new_node
                cur.next = new_node
                self.s += 1
                return
            cur = cur.next
        print("مقدار مورد نظر پیدا نشد")

    def push_back(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.s += 1

    def pop_back(self):
        if self.tail is None:
            print("استک خالی")
            return -1
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
            self.s -= 1
        else:
            self.head = None
            self.s = 0
        return data

    def back(self):
        if self.tail is None:
            print("استک خالی")
            return -1
        return self.tail.data

    def size(self):
        return self.s

    def is_empty(self):
        return self.head is None

    def print_all(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

class stack:
    def __init__(self, faza):
        self.faza = faza
        self.a = doublelinklist(faza)

    def push(self, data):
        if self.a.size() >= self.faza:
            print("پر هست استک")
            return -1
        self.a.push_back(data)

    def pop(self):
        return self.a.pop_back()

    def top(self):
        return self.a.back()

    def is_empty(self):
        return self.a.is_empty()

    def force_insert(self, data):
        self.a.push_back(data)

    def print_all(self):
        self.a.print_all()

def count_even(linked_list_object):
    even_count = 0
    current_node = linked_list_object.head

    while current_node:
        if current_node.data % 2 == 0:
            even_count += 1
        current_node = current_node.next

    return even_count

def count_even2(stack_object):
    even_count = 0
    print("even nums")

    current_node = stack_object.a.head
    while current_node:
        if current_node.data % 2 == 0:
            print(current_node.data, end=" ")
            even_count += 1
        current_node = current_node.next

    print()
    print(f"total even nums {even_count}")
    return even_count

test_stack = stack(10)

for _ in range(10):
    r = random.randint(1, 20)
    test_stack.push(r)

result = count_even2(test_stack)