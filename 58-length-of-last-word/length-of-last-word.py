class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = s.split()[-1]
        return len(last)
        