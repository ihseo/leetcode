from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        max_candies = max(candies)
        for num in candies:
            if num + extraCandies >= max_candies:
                output.append(True)
            else:
                output.append(False)
        return output