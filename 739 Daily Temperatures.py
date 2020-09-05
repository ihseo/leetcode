from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        output = [0] * len(T)
        stack = []
        for i, num in enumerate(T):
            while stack and stack[-1][1] < num:
                index, number = stack.pop()
                output[index] = i - index
            stack.append((i, num))
        return output