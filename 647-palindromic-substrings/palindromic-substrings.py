"""
string s가 주어졌을 때, s에서 나올 수 있는 palindrome의 조건을 만족하는 substring 개수를 구하라.
(s는 전부 소문자, 1이상 1000이하)

1. 완전 탐색
- 나올 수 있는 모든 경우의 수 substring을 만들어 palindrome의 조건을 만족하는지 계산

TC: O(N^3)
SC: O(N)

2. 최적화 - 중심 확장
- 모든 palindrome은 어떤 중심을 기준으로 좌우 대칭인 원리를 이용
=> 문자열의 모든 위치를 중심으로 삼고, 양쪽으로 좌우를 확장하며 검사하면 됨
- 중심 개수: 2n - 1

TC: O(N^2)
SC: O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)

        def expandAroundCenter(left: int, right: int):
            nonlocal cnt  # 중첩 함수에서 바깥 함수의 지역 변수에 접근할 때 사용
            while left >= 0 and right < n and s[left] == s[right]:  # 범위를 벗어나지 않고, 팰린드롬 조건을 충족하면
                # 확장
                cnt += 1
                left -= 1
                right += 1

        for center in range(n):
            expandAroundCenter(center, center)  # 홀수 길이
            expandAroundCenter(center, center + 1)  # 짝수 길이

        return cnt
