class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def dfs(picked, unpicked):
            if not unpicked:
                return permutations.append(picked)
            for i, num in enumerate(unpicked):
                dfs(picked + [num], unpicked[:i] + unpicked[i+1:])

        dfs([], nums)

        return permutations