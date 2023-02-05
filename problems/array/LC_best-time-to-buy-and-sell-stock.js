/** https://leetcode.com/problems/best-time-to-buy-and-sell-stock */

 /**
  * O(N^2). Time Limit Exceeded.
  * prices의 length가 최대 10^5이므로 O(N^2)로는 할 수 없다.
  */
 var maxProfit = function(prices) {
  let maxProfit = 0

  prices.forEach((price, buy) => {
      for (let sell = buy + 1; sell < prices.length; sell++) {
          maxProfit = Math.max(prices[sell] - prices[buy], maxProfit)
      }
  })

  return maxProfit
};