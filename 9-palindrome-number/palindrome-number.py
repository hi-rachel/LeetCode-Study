class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        x_len = len(x)
        for i in range(0, x_len//2):
            if x[i] != x[x_len-i-1]:
                return False
        return True