from collections import defaultdict, deque

class FreqStack:

    def __init__(self):
        self.freq_map = defaultdict(int)
        self.stack = {}
        self.deque = deque()

    def push(self, val: int) -> None:
        self.freq_map[val] += 1
        if self.freq_map[val] not in self.stack:
            self.stack[self.freq_map[val]] = [val]
        else:
            self.stack[self.freq_map[val]].append(val)
        self.deque.append(val)

    def pop(self) -> int:
        max_freq = max(self.freq_map.values())
        max_val = self.stack[max_freq].pop()
        if not self.stack[max_freq]:
            del self.stack[max_freq]
        self.freq_map[max_val] -= 1
        self.deque.remove(max_val)
        return max_val
