"""
string s가 주어졌을 때, s에서 나올 수 있는 palindrome의 조건을 만족하는 substring 개수를 구하라.
(s는 전부 소문자, 1이상 1000이하)

1. 완전 탐색
- 나올 수 있는 모든 경우의 수 substring을 만들어 palindrome의 조건을 만족하는지 계산
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)

        def isPalindrome(test):
            return test == test[::-1]

        for i in range(n):
            for j in range(i+1, n+1):
                if isPalindrome(s[i:j]):
                    cnt += 1

        return cnt
