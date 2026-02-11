class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.down = None
        self.up = None

class FourDimensionalLinkedList:
    def __init__(self):
        self.head = None


    def is_empty(self):
        return self.head is None


    def add_first(self, data):
        new_node = Node(data)
        if not self.is_empty():
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node


    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp


    def remove_first(self):
        if self.is_empty():
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return value


    def remove_last(self):
        if self.is_empty():
            return None
        temp = self.head
        while temp.next:
            temp = temp.next
        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None
        return temp.data


    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False


    def count(self):
        cnt = 0
        temp = self.head
        while temp:
            cnt += 1
            temp = temp.next
        return cnt


    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


    def add_down(self, parent_data, child_data):
        temp = self.head
        while temp:
            if temp.data == parent_data:
                temp.down = Node(child_data)
                return
            temp = temp.next


    def add_up(self, parent_data, child_data):
        temp = self.head
        while temp:
            if temp.data == parent_data:
                temp.up = Node(child_data)
                return
            temp = temp.next


    def remove_down(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                temp.down = None
                return
            temp = temp.next


    def remove_up(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                temp.up = None
                return
            temp = temp.next


    def has_down(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return temp.down is not None
            temp = temp.next
        return False


    def has_up(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return temp.up is not None
            temp = temp.next
        return False


    def clear(self):
        self.head = None