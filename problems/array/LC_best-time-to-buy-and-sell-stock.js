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

 /**
  * O(N).
  * 산 가격보다 판 가격이 더 적어 profit이 0보다 작다면, 차라리 판 날짜에서 사는 게 더 낫다. 따라서 살 날짜를 팔 날짜로 이동한다.
  * 이 때 팔 날짜는 그냥 +1해준다.
  * 만약 profit이 0보다 크다면 산 날짜는 가만히 있는다. 더 좋은 결과를 기대해 볼 수 있으므로. 대신 팔 날짜를 움직여서 profit이 더 커지는 때를 노려본다.
  */
 var maxProfit = function(prices) {
  let maxProfit = 0
  let buyIdx = 0
  let sellIdx = 1

  while (buyIdx < sellIdx) {
      if (sellIdx >= prices.length) {
          break
      }

      const profit = prices[sellIdx] - prices[buyIdx]
      if (profit < 0) {
          buyIdx = sellIdx
      }

      if (profit > maxProfit) {
          maxProfit = profit
      }

      sellIdx++
  }

  return maxProfit
};