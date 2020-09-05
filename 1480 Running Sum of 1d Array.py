from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        total = 0
        for num in nums:
            total += num
            answer.append(total)
        return answer
