class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = s.strip().split()[-1]
        return len(last)
        