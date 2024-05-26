/**
 * @param {number[]} nums
 * @return {number}
 */

// 중복을 제거해라, 순서는 유지, nums의 고유 숫자 개수를 반환해라

var removeDuplicates = function(nums) {
    idx = 0
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] != nums[idx]) {
            idx += 1
            nums[idx] = nums[i]
        }
    }
    return idx + 1
};