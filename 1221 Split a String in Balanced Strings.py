class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, num_L, num_R = 0, 0, 0
        for letter in s:
            if letter == 'L':
                num_L += 1
            else:
                num_R += 1
            if num_L != 0 and num_L == num_R:
                count += 1
        return count