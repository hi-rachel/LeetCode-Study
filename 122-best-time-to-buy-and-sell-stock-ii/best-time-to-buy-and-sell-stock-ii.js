/**
 * @param {number[]} prices
 * @return {number}
 */

var maxProfit = function(prices) {
    let max = 0;
    let start = prices[0];
    let len = prices.length;

    for (let i = 1; i < len; i++) {
        if (start < prices[i]) {
            max += prices[i] - start;
        }
        start = prices[i];
    }
    return max;
};