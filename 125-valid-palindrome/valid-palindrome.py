class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''.join(char.lower() for char in s if char.isalnum())
        if clean_str == clean_str[::-1]:
            return True
        else:
            return False