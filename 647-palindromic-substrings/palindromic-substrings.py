"""
“모든 회문은 중심에서 좌우 대칭이다”
→ 따라서 모든 중심점에서 좌우로 확장하면서 회문인지 확인하면
→ 모든 회문 substring을 탐색 가능!
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for center in range(len(s)):
            print(center)
            count += self.expand(s, center, center)

            count += self.expand(s, center, center + 1)
        return count

    def expand(self, s, left, right):
        count = 0
        # 범위를 벗어나지 않고, palindrome이면 확장
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
