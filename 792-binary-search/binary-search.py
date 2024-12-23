# 오름차순으로 정렬된 nums
# target이 존재하면 해당 index, 존재하지 않으면 -1 반환
# O(log n) 시간 복잡도로 구현해라

def binary_search(nums, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] > target:
        return binary_search(nums, target, low, mid - 1)
    if nums[mid] < target:
        return binary_search(nums, target, mid + 1, high)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target, 0, len(nums)-1)