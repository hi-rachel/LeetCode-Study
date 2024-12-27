class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            low, high = i + 1, len(numbers) - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[i] + numbers[mid] == target:
                    return [i + 1, mid + 1]
                if numbers[i] + numbers[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1