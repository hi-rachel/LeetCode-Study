"""
문자열 s가 주어졌을 때, 중복된 문자를 제거하고 가장 긴 연속된 substring을 찾아라

1. 첫번째 풀이

Hint!
Generate all possible substrings & check for each substring if it's valid and keep updating maxLen accordingly.

TC: O(N^3)
SC: O(N)
=> Time Limit Exceeded

2. 최적화 - 슬라이딩 윈도우 + 해시셋
- 슬라이딩 윈도우: 문자열 내에서 left, right 포인터로 범위를 정하고 점진적으로 이동
- 해시셋: 현재 윈도우에 어떤 문자가 있는지 빠르게 체크 가능
- 중복 문자가 등장하면 왼쪽 포인터를 이동시켜서 중복을 제거

TC: O(N)
SC: O(N)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # 현재 윈도우에 있는 문자들
        left = 0
        max_len = 0

        for right in range(len(s)):
            # 중복 문자가 나오면 왼쪽 포인터를 이동시켜 중복 제거
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # 중복이 없으면 윈도우에 추가
            char_set.add(s[right])

            # 최대 길이 갱신
            max_len = max(max_len, right - left + 1)
            
        return max_len