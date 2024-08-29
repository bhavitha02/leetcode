# https://leetcode.com/problems/house-robber/description/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = 0
        otp = []
        for i in range(0, len(nums), 2):
            val +=nums[i]
        otp.append(val)
        val = 0
        for i in range(1, len(nums), 2):
            val +=nums[i]
        otp.append(val)
        return max(otp)
