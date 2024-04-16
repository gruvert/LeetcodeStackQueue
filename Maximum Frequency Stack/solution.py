from collections import defaultdict, deque
class FreqStack:
    def __init__(self):
        self.dicti = defaultdict(int)
        self.stack = {}
        self.deque = deque()
    def push(self, val: int) -> None:
        self.dicti[val] += 1
        if self.dicti[val] not in self.stack:
            self.stack[self.dicti[val]] = [val]
        else:
            self.stack[self.dicti[val]].append(val)
        self.deque.append(val)
    def pop(self) -> int:
        max_freq = max(self.dicti.values())
        max_val = self.stack[max_freq].pop()
        if not self.stack[max_freq]:
            del self.stack[max_freq]
        self.dicti[max_val] -= 1
        self.deque.remove(max_val)
        return max_val
