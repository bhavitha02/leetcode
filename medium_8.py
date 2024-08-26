# https://leetcode.com/problems/word-break/description/
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        start = 0
        count = 0
        for i in wordDict:
            word_len =  start + len(i)
            if i == s[start:word_len]:
                start = word_len
                count += 1
            else:
                return False
            if count == len(wordDict):
                return True

        
