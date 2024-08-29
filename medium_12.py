# https://leetcode.com/problems/coin-change/description/
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        i = len(coins)-1
        otp = 0
        if i == 0 and coins[i]>amount:
            return 0
        if i == 0 and coins[i]<amount:
            

        while amount > 0:
            if coins[i]>amount:
                i -= 1
            else:
                amount = amount - coins[i]
                otp = otp + 1
        return otp
