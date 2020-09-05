class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        num = k if len(self.stack) >= k else len(self.stack)
        for i in range(num):
            self.stack[i] += val

a = CustomStack(3)
a.push(1)
a.push(2)
a.push(3)
a.increment(10, 100)
print(a)