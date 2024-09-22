class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        rev_num = original[::-1]
        if original == rev_num:
            return True
        return False
