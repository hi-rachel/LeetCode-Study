"""
너비: e - s
높이: min(height[s], height[e])

넓이 = e - s * min(height[s], height[e])
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        s, e = 0, len(height) - 1
        while s < e:
            area = (e - s) * min(height[s], height[e])
            max_area = max(area, max_area)
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1

        return max_area
