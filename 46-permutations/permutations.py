import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list(itertools.permutations(nums, len(nums)))
        return result