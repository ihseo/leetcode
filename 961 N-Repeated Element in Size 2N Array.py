from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        my_dict = {key: 0 for key in set(A)}

        for element in A:
            my_dict[element] += 1

        return max(my_dict, key=my_dict.get)