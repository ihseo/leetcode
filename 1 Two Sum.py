from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            num_map[num] = i
        print(num_map)

        for i, num in enumerate(nums):
            if target - num in num_map and i != num_map[target - num]:
                return nums.index(num), num_map[target - num]
        return 0, 0
sol = Solution()
print(sol.twoSum([3,1], target=6))