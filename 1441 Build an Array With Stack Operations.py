from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        i = 1
        for num in target:
            if num != i:
                for _ in range(num - i):
                    output.append("Push")
                    output.append("Pop")
            output.append("Push")
            i = num + 1
            if num == n:
                break
        return output