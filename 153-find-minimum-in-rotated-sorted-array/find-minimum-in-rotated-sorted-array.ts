function findMin(nums: number[]): number {
    let low = 0, high = nums.length;

    while (low <= high) {
        let mid = (low + high) // 2
        if (nums[mid - 1] > nums[mid]) {
            return nums[mid]
        }
        if (nums[0] < nums[mid]) {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return nums[0]
};      