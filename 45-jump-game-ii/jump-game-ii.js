/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let cnt = 0;
    let prev = 0;
    let max = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        max = Math.max(max, i + nums[i]);
        if (i === prev) {
            cnt++;
            prev = max;
        }
    }
    return cnt;
};