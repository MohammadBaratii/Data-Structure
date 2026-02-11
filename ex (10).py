class AdvancedStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def clear(self):
        self.stack.clear()

    def contains(self, x):
        return x in self.stack

    def reverse(self):
        self.stack.reverse()

    def copy(self):
        return self.stack.copy()

    def get_min(self):
        return min(self.stack) if not self.is_empty() else None

    def get_max(self):
        return max(self.stack) if not self.is_empty() else None

    def sum(self):
        return sum(self.stack)

    def average(self):
        if self.is_empty():
            return None
        return sum(self.stack) / self.size()

    def count_even(self):
        return sum(1 for x in self.stack if x % 2 == 0)

    def count_odd(self):
        return sum(1 for x in self.stack if x % 2 != 0)

    def remove_duplicates(self):
        self.stack = list(dict.fromkeys(self.stack))

    def sort_ascending(self):
        self.stack.sort()

    def sort_descending(self):
        self.stack.sort(reverse=True)

    def prioritize(self):
        self.sort_descending()

    def push_multiple(self, items):
        for x in items:
            self.push(x)

    def pop_multiple(self, k):
        result = []
        for _ in range(min(k, self.size())):
            result.append(self.pop())
        return result

    def is_palindrome(self):
        return self.stack == self.stack[::-1]

    def get_middle(self):
        if self.is_empty():
            return None
        return self.stack[self.size() // 2]

    def replace(self, old, new):
        self.stack = [new if x == old else x for x in self.stack]

    def remove_value(self, x):
        self.stack = [v for v in self.stack if v != x]

    def frequency(self, x):
        return self.stack.count(x)

    def max_frequency(self):
        if self.is_empty():
            return None
        return max(set(self.stack), key=self.stack.count)

    def min_frequency(self):
        if self.is_empty():
            return None
        return min(set(self.stack), key=self.stack.count)

    def push_if_unique(self, x):
        if x not in self.stack:
            self.push(x)

    def swap_top(self):
        if self.size() < 2:
            return
        self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def rotate_left(self):
        if self.size() > 1:
            self.stack.append(self.stack.pop(0))

    def rotate_right(self):
        if self.size() > 1:
            self.stack.insert(0, self.stack.pop())

    def to_string(self):
        return " ".join(map(str, self.stack))

    def info(self):
        return {
            "size": self.size(),
            "is_empty": self.is_empty(),
            "top": self.peek()
        }