/**
 * @param {number[]} nums
 * @return {boolean}
 */

var canJump = function(nums) {
    goal = nums.length - 1;

    for (let i = goal; i >= 0; i--) {
        if (i + nums[i] >= goal)
            goal = i;
        }

    if (goal === 0) return true;
    else return false;
};