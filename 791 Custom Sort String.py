class Solution:
    def customSortString(self, S: str, T: str) -> str:
        answer = []
        count_dict = {}
        for letter in T:
            count_dict[letter] = count_dict.get(letter, 0) + 1

        for letter in S:
            if letter in count_dict:
                for _ in range(count_dict[letter]):
                    answer.append(letter)
                count_dict[letter] = 0

        for letter, v in count_dict.items():
            if v > 0:
                for _ in range(count_dict[letter]):
                    answer.append(letter)
                count_dict[letter] -= 1

        return ''.join(answer)


sol = Solution()
print(sol.customSortString("cba", "abcd"))