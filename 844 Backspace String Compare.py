class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack = []
        stack2 = []
        for letter in S:
            if letter == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(letter)

        for letter in T:
            if letter == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(letter)

        return stack == stack2