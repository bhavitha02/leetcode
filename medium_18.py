# https://leetcode.com/problems/course-schedule/description/
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        cnt = 0
        for i in range(len(prerequisites)):
            for j in range(1, len(prerequisites)-1):
                if prerequisites[i][1] == prerequisites[j][0] and prerequisites[i][0] == prerequisites[j][1]:
                    continue
                else:
                    
                

