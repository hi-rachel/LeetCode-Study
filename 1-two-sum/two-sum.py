class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            rest = target - nums[i]
            rest_nums = nums[i+1:]
            if rest in rest_nums:
                result.append(i)
                result.append(rest_nums.index(rest)+i+1)
                break
        return result