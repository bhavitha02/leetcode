# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = []
        otp = []
        tmp = ''
        for i in s:
            if i not in tmp:
                tmp+=i
            else:
                 lst.append(tmp)
                 tmp = i
        for j in lst:
            otp.append(len(j))
        if otp:
            return max(otp)
        else:
          return 0
       
        


