class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            return s[left + 1 : right]

        res = ""
        for i in range(len(s)):
            temp1 = expand(i, i)    # 홀수 길이 팰린드롬
            temp2 = expand(i, i+1)  # 짝수 길이 팰린드롬
            if len(temp1) > len(res):
                res = temp1
            if len(temp2) > len(res):
                res = temp2
        return res
