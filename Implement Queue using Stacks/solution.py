class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        item = self.head.data
        self.head = self.head.next
        return item

    @property
    def peek(self):
        return self.head.data

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, data):
        self.s1.push(data)

    def pop(self):
        cur = self.s1.head
        while cur:
            if self.s1.peek:
                self.s2.push(self.s1.pop())
            cur = cur.next
        m = self.s2.pop()
        cur = self.s2.head
        while cur:
            if self.s2.peek:
                self.s1.push(self.s2.pop())
            cur = cur.next
        return m

    def peek(self):
        cur = self.s1.head
        while cur:
            self.s2.push(self.s1.pop())
            cur = cur.next
        out = self.s2.peek 
        cur = self.s2.head
        while cur:
            self.s1.push(self.s2.pop())
            cur = cur.next
        return out

    def empty(self):
        return self.s1.is_empty()
