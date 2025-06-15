class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        for interval in sorted(intervals):
            if not output or output[-1][1] < interval[0]:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], interval[1])
        
        return output