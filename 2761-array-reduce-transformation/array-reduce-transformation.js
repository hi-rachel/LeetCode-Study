/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    num_sum = init
    for (let i = 0; i < nums.length; i++) {
        num_sum = fn(num_sum, nums[i])
    }
    return num_sum
};