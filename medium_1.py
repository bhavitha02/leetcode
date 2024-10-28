# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        #  Sol 1: O(n) = n^2
        # if len(prices)<=1:
        #     return 0
        # max_value = 0
        # for i in range(len(prices)-1):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         sell = prices[j]
        #         diff = sell - buy
        #         if diff > max_value:
        #             max_value = diff
                
        # return max(max_value, 0)
        # Sol 2: O(n) = n 
          mini = [prices[0]]
          for i in range(1, len(prices)):
              mini.append(min(mini[-1], prices[i-1]))
          return max([i-j for i, j in zip(prices, mini)])
        # Sol 3: O(n) = n Sliding window technique
          buy = 0
          max_profit = 0
          for sell in range(1, len(prices)):
              if prices[buy] < prices[sell]:
                  current_profit = prices[sell] - prices[buy]
                  max_profit = max(current_profit, max_profit)
              else:
                  buy = sell
          return max_profit
        
        



