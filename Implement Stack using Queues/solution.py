class Node:
    def __init__(self, item, next=None):
        self.data = item
        self.next = next
class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    def push(self, x: int) -> None:
        self.q1.add(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.add(self.q1.pop().data)
        popped = self.q1.pop().data
        while not self.q2.is_empty():
            self.q1.add(self.q2.pop().data)
        return popped

    def top(self) -> int:
        return self.q1.tail.data

    def empty(self) -> bool:
        return self.q1.is_empty()

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        item = self.head
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
    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.data)+' '
            current = current.next
        return f'start -> {s}<- end'
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
