class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = address.split('.')
        return '[.]'.join(defanged)