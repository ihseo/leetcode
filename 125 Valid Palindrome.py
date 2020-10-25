class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([x for x in s if x.isalnum()])
        if s.lower() == s[::-1].lower():
            return True
        return False

a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))
print(a.isPalindrome("0P"))
print(a.isPalindrome(""))