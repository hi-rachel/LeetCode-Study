"""
주어진 정수 배열 nums에서 가장 긴 증가하는 부분 수열의 길이를 구하는 문제

이분 탐색 풀이 - TC: O(n log n), SC: O(n)

# bisect란?
bisect는 Python의 표준 라이브러리로 정렬된 리스트에 이진 탐색으로 원소를 삽입할 위치를 찾는 모듈.

bisect_left(arr, x):
- x를 삽입할 가장 왼쪽 위치를 반환
- 즉, arr에서 x보다 크거나 같은 첫 번째 위치 (인덱스)를 반환
- 정렬 상태를 유지하며 x를 끼워 넣는 위치를 찾음
"""
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [] # 각 길이별 증가 수열의 마지막 값(가장 작은 값)을 저장
        for num in nums:
            idx = bisect.bisect_left(tail, num)
            if idx == len(tail):
                tail.append(num)
            else:
                tail[idx] = num # 수열 길이 늘림 혹은 수열 시작이 더 작은 값이 있다면 바꾸기
        return len(tail)