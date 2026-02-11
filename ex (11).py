class MegaStack:

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
        return None if self.is_empty() else self.stack[-1]

    def clear(self):
        self.stack.clear()

    def copy(self):
        return self.stack.copy()

    def to_list(self):
        return list(self.stack)

    def contains(self, x):
        return x in self.stack

    
    def get_min(self):
        return min(self.stack) if not self.is_empty() else None

    def get_max(self):
        return max(self.stack) if not self.is_empty() else None

    def get_sum(self):
        return sum(self.stack)

    def average(self):
        return self.get_sum() / self.size() if not self.is_empty() else None

    def count_even(self):
        return sum(1 for x in self.stack if x % 2 == 0)

    def count_odd(self):
        return sum(1 for x in self.stack if x % 2 != 0)

    def frequency(self, x):
        return self.stack.count(x)

    def max_frequency(self):
        return max(set(self.stack), key=self.stack.count) if self.stack else None

    def min_frequency(self):
        return min(set(self.stack), key=self.stack.count) if self.stack else None

    def unique_count(self):
        return len(set(self.stack))

    
    def sort_ascending(self):
        self.stack.sort()

    def sort_descending(self):
        self.stack.sort(reverse=True)

    def prioritize(self):
        self.sort_descending()

    def remove_duplicates(self):
        self.stack = list(dict.fromkeys(self.stack))

    def push_if_unique(self, x):
        if x not in self.stack:
            self.push(x)

    def replace(self, old, new):
        self.stack = [new if x == old else x for x in self.stack]

    def remove_value(self, x):
        self.stack = [v for v in self.stack if v != x]

    def get_middle(self):
        return self.stack[self.size() // 2] if not self.is_empty() else None

    def is_sorted(self):
        return self.stack == sorted(self.stack)

    def reverse(self):
        self.stack.reverse()

    
    def push_multiple(self, items):
        for x in items:
            self.push(x)

    def pop_multiple(self, k):
        result = []
        for _ in range(min(k, self.size())):
            result.append(self.pop())
        return result

    def swap_top(self):
        if self.size() >= 2:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def rotate_left(self):
        if self.size() > 1:
            self.stack.append(self.stack.pop(0))

    def rotate_right(self):
        if self.size() > 1:
            self.stack.insert(0, self.stack.pop())

    def duplicate_top(self):
        if not self.is_empty():
            self.push(self.peek())

    def remove_top(self):
        if not self.is_empty():
            self.pop()

    def bottom(self):
        return self.stack[0] if not self.is_empty() else None

    def remove_bottom(self):
        if not self.is_empty():
            self.stack.pop(0)

    def insert_bottom(self, x):
        self.stack.insert(0, x)

    
    def is_palindrome(self):
        return self.stack == self.stack[::-1]

    def all_positive(self):
        return all(x > 0 for x in self.stack)

    def any_negative(self):
        return any(x < 0 for x in self.stack)

    def find_index(self, x):
        return self.stack.index(x) if x in self.stack else -1

    def count_greater_than(self, k):
        return sum(1 for x in self.stack if x > k)

    def count_less_than(self, k):
        return sum(1 for x in self.stack if x < k)

    def map_square(self):
        self.stack = [x * x for x in self.stack]

    def filter_even(self):
        self.stack = [x for x in self.stack if x % 2 == 0]

    def filter_odd(self):
        self.stack = [x for x in self.stack if x % 2 != 0]

    def sum_top_k(self, k):
        return sum(self.stack[-k:])

    def compare_size(self, other):
        return self.size() - other.size()

    def merge(self, other):
        self.push_multiple(other.to_list())

    def equals(self, other):
        return self.stack == other.to_list()

    def clear_if_full(self, limit):
        if self.size() >= limit:
            self.clear()

    def trim(self, k):
        self.stack = self.stack[:k]

    
    def to_string(self):
        return " ".join(map(str, self.stack))

    def print_stack(self):
        print(self.stack)

    def info(self):
        return {
            "size": self.size(),
            "is_empty": self.is_empty(),
            "top": self.peek()
        }

    def memory_usage(self):
        return self.size() * 8

    def reset(self):
        self.clear()

    def clone(self):
        new = MegaStack()
        new.push_multiple(self.stack)
        return new

    def push_range(self, a, b):
        for i in range(a, b + 1):
            self.push(i)

    def remove_range(self, a, b):
        self.stack = [x for x in self.stack if not (a <= x <= b)]

    def count_range(self, a, b):
        return sum(1 for x in self.stack if a <= x <= b)

    def checksum(self):
        return hash(tuple(self.stack))