class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        max_len = 0

        for right in range(len(s)):
            char = s[right]

            if char in seen and seen[char] >= left:
                left = seen[char] + 1

            seen[char] = right

            max_len = max(max_len, right - left + 1)

        return max_len