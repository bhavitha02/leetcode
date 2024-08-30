# https://leetcode.com/problems/merge-intervals/description/
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        lst = [intervals[0]]
        for i in range(len(intervals)-1):
            if lst[-1][1] >= intervals[i+1][0] and lst[-1][0] <= intervals[i+1][0]:
                lst[-1][1] = intervals[i+1][1]
            elif lst[-1][1] >= intervals[i+1][0] and lst[-1][0] > intervals[i+1][0] and lst[-1][1] <= intervals[i+1][1]:
                lst[-1][1] = intervals[i+1][1]
                lst[-1][0] = intervals[i+1][0]
            elif lst[-1][1] >= intervals[i+1][0] and lst[-1][0] > intervals[i+1][0] and lst[-1][1] >= intervals[i+1][1]:
                lst[-1][0] = intervals[i+1][0]
                
            else:
                lst.append(intervals[i+1])
        return lst
