function missingNumber(nums: number[]): number {
    const expectedSum = Math.floor(nums.length * (nums.length + 1) / 2);
    const actualSum = nums.reduce((acc, cur) => acc + cur);
    return expectedSum - actualSum;
};