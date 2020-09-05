from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for number in nums:
            count = 0
            for num in nums:
                if number > num:
                    count += 1
            output.append(count)

        return output
