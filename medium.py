# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
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
        # [1,2,4,5,8,9]
        # [1, 1, 1, 1, 1, 1]
        # [10,15,7,8,10,1,2,3]
        # [10,10,10,7,7,7,1,1]
        mini = [prices[0]]
        for i in range(1, len(prices)):
            mini.append(min(mini[-1], prices[i-1]))
        return max([i-j for i, j in zip(prices, mini)])

        # time complexity is O(n)
        # space complexity is O(n)




