/**
 * 주식 수익이 최대가 될 수 있게 주식을 살 날과 이후에 주식을 팔 날을 골라
 * 최대 주식 수익을 반환해라, 수익을 얻을 수 없다면 0 반환
 *
 * TC: O(N)
 * SC: O(1)
 */

function maxProfit(prices: number[]): number {
    let max_profit: number = 0;
    let min_price: number = prices[0];

    for (let price of prices) {
        min_price = Math.min(min_price, price);
        max_profit = Math.max(max_profit, price - min_price);
    }
    return max_profit;
};