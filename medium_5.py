# https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lar_sum = 0
        lst = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                lar_sum += nums[j]
                lst.append(lar_sum)
            lar_sum = 0
        final = lst[0]
        for k in lst[1:]:
            if final < k:
                final = k
        return final
