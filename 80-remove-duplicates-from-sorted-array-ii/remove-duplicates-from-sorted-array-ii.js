/**
 * @param {number[]} nums
 * @return {number}
 */

var removeDuplicates = function(nums) {
    if (nums.length <= 2) {
        return nums.length;
    }

    k = 2

    for (let i = 2; i < nums.length; i++) {
        if ((nums[k-1] !== nums[i]) || (nums[k-2] !== nums[i])) {
            nums[k] = nums[i];
            k += 1;
        }
    }
    return k;
};