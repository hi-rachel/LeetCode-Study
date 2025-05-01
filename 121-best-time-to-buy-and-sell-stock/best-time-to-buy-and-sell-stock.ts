function maxProfit(prices: number[]): number {
    let max_profit: number = 0;
    let min_price: number = prices[0];

    for (let price of prices) {
        max_profit = Math.max(max_profit, price - min_price);
        min_price = Math.min(min_price, price);
    }
    return max_profit;
};