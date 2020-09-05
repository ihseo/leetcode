from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_list = []
        list_1 = nums[:n]
        list_2 = nums[n:]
        for a, b in zip(list_1, list_2):
            shuffled_list.append(a)
            shuffled_list.append(b)

        return shuffled_list