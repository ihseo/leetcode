class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        self.stack = []
        for char in S:
            if char == '(':
                self.stack.append(char)
            else:    # else is always '('
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
                else:
                    self.stack.append(char)

        return len(self.stack)

