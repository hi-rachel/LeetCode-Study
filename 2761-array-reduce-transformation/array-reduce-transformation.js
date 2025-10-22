/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    num_sum = init;
    nums.forEach(num => {
        num_sum = fn(num_sum, num);
    });
    return num_sum;
};