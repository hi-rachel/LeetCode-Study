function rob(nums: number[]): number {
    if (nums.length === 0) return 0;
    if (nums.length === 1) return nums[0];

    const dp: number[] = new Array(nums.length).fill(0);
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0], nums[1]);

    for (let i = 2; i < nums.length; i++) {
        dp[i] = Math.max(dp[i - 1], nums[i] + dp[i - 2]);
    }

    return dp[nums.length - 1];
}