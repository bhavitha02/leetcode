# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution(object):
    def find_longest_substring(input_str):
        hash_map = {}
        start = 0 
        len_current_window = 0
        longest_len = 0
        for i in range(len(input_str)):
            if input_str[i] in hash_map:
                if hash_map[input_str[i]] < start:
                    len_current_window = i - start + 1
                    hash_map[input_str[i]] = i
                else:
                    start = hash_map[input_str[i]]
                    start+=1
                    hash_map[input_str[i]] = i
                    len_current_window = i - start + 1
            else:
                hash_map[input_str[i]]=i
                len_current_window = i - start + 1
            longest_len = max(len_current_window, longest_len)
        return longest_len
    
       
        


