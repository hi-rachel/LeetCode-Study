/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = (function(n) {
    const memo = {}

    return function(n) {
        if (n in memo) return memo[n];
        if (n < 3) return n;
        memo[n] = climbStairs(n - 1) + climbStairs(n - 2);
        return memo[n];
    };
})();