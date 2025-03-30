/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let indices = new Map();

    for (let i = 0; i < nums.length; i++) {
        diff = target - nums[i];
        if (indices.has(diff)) {
            return [i, indices.get(diff)];
        }
        indices.set(nums[i], i);
    }
};