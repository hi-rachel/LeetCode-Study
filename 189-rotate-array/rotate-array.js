/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
   k = k % nums.length;
   if (k != 0) {
    let arr = [];
    for (let i = nums.length - k; i < nums.length; i++) {
        arr.push(nums[i])
    }
    for (let i = 0; i < nums.length - k; i++) {
        arr.push(nums[i])
    }
    for (let i = 0;  i< nums.length; i++) {
        nums[i] = arr[i];
    }
   }
};