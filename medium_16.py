# https://leetcode.com/problems/merge-intervals/description/
class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals,key=lambda x:x[0])
        output_list = [intervals[0]]
        for i in intervals[1:]:
            if i[0]<=output_list[-1][1]:
                if i[1]>output_list[-1][1]:
                    output_list[-1][1] = i[1]
            else:
                output_list.append(i)
        return output_list
