from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_dict = Counter(arr)
        return len(my_dict) == len(set(my_dict.values())) 