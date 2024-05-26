/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count = 0, maj = 0;
    for (let n of nums) {
        if (count === 0) {
            maj = n;
        }
        if (maj === n) {
            count++;
        } else {
            count--;
        }
    }
    return maj;
};