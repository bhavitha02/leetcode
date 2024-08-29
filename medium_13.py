# https://leetcode.com/problems/jump-game/description/
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)-1
        route = 0
        for i in range(n):
            route = i + nums[i]
            if nums[route]==0:
                return False
            while route<n:
                route += nums[route]
                if nums[route]==0:
                    return False
            if route == n:
                return True


        
