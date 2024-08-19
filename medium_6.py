# https://leetcode.com/problems/climbing-stairs/description/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = [1,2]
        if n<3:
            return n
        else:
            for i in range(2, n):
                sum = lst[-1] + lst[-2]
                lst.append(sum)
            return lst[-1]

