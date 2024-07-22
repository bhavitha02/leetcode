# Product of array except itself 
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = []
        if len(nums)<1:
            return nums[0]
        else:
            for i in range(len(nums)):
                dup = nums
                del dup[i]
                prod = dup[0]
                for j in dup[1:]:
                    prod *= j
                lst.append(prod)
        return prod
                
