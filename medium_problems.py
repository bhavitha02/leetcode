# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# best time to buy and sell stock
class Solution(object):
    def maxProfit(self, prices):
        #  Sol 1: O(n) = n^2
        # if len(prices)<=1:
        #     return 0
        # max_value = 0
        # for i in range(len(prices)-1):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         sell = prices[j]
        #         diff = sell - buy
        #         if diff > max_value:
        #             max_value = diff
                
        # return max(max_value, 0)
        # Sol 2: O(n) = n 
          mini = [prices[0]]
          for i in range(1, len(prices)):
              mini.append(min(mini[-1], prices[i-1]))
          return max([i-j for i, j in zip(prices, mini)])
        # Sol 3: O(n) = n Sliding window technique
          buy = 0
          max_profit = 0
          for sell in range(1, len(prices)):
              if prices[buy] < prices[sell]:
                  current_profit = prices[sell] - prices[buy]
                  max_profit = max(current_profit, max_profit)
              else:
                  buy = sell
          return max_profit
        
# contains duplicate        
# https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new = set(nums)
        if len(new)==len(nums):
            return False
        return True


# two sum problem
# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, value in enumerate(nums):
            cmpt = target - value
            if cmpt in nums[i+1:]:
                return (i, nums.index(cmpt, i+1))

# https://leetcode.com/problems/product-of-array-except-self/
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
                
# https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lar_sum = 0
        lst = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                lar_sum += nums[j]
                lst.append(lar_sum)
            lar_sum = 0
        final = lst[0]
        for k in lst[1:]:
            if final < k:
                final = k
        return final


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

# https://leetcode.com/problems/longest-increasing-subsequence/description/
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = []
        dummy = nums[0]
        for i in range(1, len(nums)):
            if nums[i]<dummy:
                dummy = nums[i]
                lst.append(dummy)


# https://leetcode.com/problems/unique-paths/description/

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        pass



# https://leetcode.com/problems/house-robber-ii/description/


        
# https://leetcode.com/problems/house-robber/description/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = 0
        otp = []
        for i in range(0, len(nums), 2):
            val +=nums[i]
        otp.append(val)
        val = 0
        for i in range(1, len(nums), 2):
            val +=nums[i]
        otp.append(val)
        return max(otp)


# https://leetcode.com/problems/insert-interval/description/
class Solution(object):
    def insert(self, intervals, newInterval):
      None


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


# https://leetcode.com/problems/clone-graph/description/
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        


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

