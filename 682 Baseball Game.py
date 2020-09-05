from typing import List

def isNumber(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        total = 0
        for op in ops:
            if isNumber(op):
                stack.append(int(op))
                total += int(op)
            elif op == '+':
                num = stack[-2] + stack[-1]
                stack.append(num)
                total += num
            elif op == 'D':
                num = stack[-1] * 2
                stack.append(num)
                total += num
            elif op == 'C':
                num = stack.pop()
                total -= num

        return total
