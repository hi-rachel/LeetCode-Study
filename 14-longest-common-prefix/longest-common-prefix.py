class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        v = sorted(strs)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return common
            common += first[i]
        return common