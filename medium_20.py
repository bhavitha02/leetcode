# https://leetcode.com/problems/longest-repeating-character-replacement/description/
def characterReplacement(self, s, k):
        start, end = 0,0
        max_length = 0
        freq_char = 0
        dict_str = {}
        for i in s:
            if i in dict_str:
                dict_str[i] += 1
                end+=1
            else:
                dict_str[i] = 1
                end+=1
            freq_char = max(dict_str[i], freq_char)
            if (end-start - freq_char) > k:
                dict_str[s[start]] -= 1
                start +=1
            max_length = max(end-start,max_length)
        return max_length
