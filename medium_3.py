# Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, value in enumerate(nums):
            cmpt = target - value
            if cmpt in nums[i+1:]:
                return (i, nums.index(cmpt, i+1))
