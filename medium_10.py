# https://leetcode.com/problems/longest-increasing-subsequence/description/
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = []
        dummy = nums[0]
        for i in range(1, len(nums)):
            if nums[i]<dummy:
                dummy = nums[i]
                lst.append(dummy)
