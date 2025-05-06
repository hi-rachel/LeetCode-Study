/**
너비: (e - s)
높이: Math.min(height[s], height[e])

넓이: (e - s) * Math.min(height[s], height[e])
 */


function maxArea(height: number[]): number {
    let maxArea = 0;
    let s = 0, e = height.length - 1;
    while (s < e) {
        maxArea = Math.max((e - s) * Math.min(height[s], height[e]), maxArea)
        if (height[s] > height[e]) {
            e -= 1
        } else {
            s += 1
        }
    }
    return maxArea;
};