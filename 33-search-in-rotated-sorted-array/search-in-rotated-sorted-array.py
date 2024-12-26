# 첫 번째 범위의 마지막 값과 두 번째 범위의 첫 번째 값 사이에는 다른 값들 사이에서는 나타나지 않는 특징이 있다
# 다른 값들 사이에서는 서로 정렬되어 있는 관계이기 때문에 현재 값이 앞의 값보다 크지만
# 큰 차이를 보이는 두 값은 현재 값이 앞의 값보다 작다.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1