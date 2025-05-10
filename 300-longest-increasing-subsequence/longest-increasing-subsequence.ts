/**
new Array(n).fill(1) -> 길이가 n인 배열을 만들어, 모든 요소를 1로 채움
 */

function lengthOfLIS(nums: number[]): number {
    const n = nums.length;
    const dp = new Array(n).fill(1);  // In Python => [1] * n

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                dp[i] = Math.max(dp[j] + 1, dp[i])
            } 
        }
    }
    return Math.max(...dp)  // 숫자 배열을 펼쳐 여러 숫자를 넘겨줘야 함
};