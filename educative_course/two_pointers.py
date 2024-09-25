# valid palindrome

def is_palindrome(s):
  
  # Replace this placeholder return statement with your code
  l,r = 0, len(s)-1
  while l<=r:
    if s[l].lower()  != s[r].lower() :
      return False
    l += 1
    r -= 1 
  return True
  
      

 # 3 Sum
 def find_sum_of_three(nums, target):
   
   # Replace this placeholder return statement with your code
   nums.sort()
   for i in range(len(nums)-2):
     low = i+1
     high = len(nums)-1
     while low<high:
       if nums[i] + nums[low] + nums[high] > target:
         high-=1
       elif nums[i] + nums[low] + nums[high] < target:
         low+=1
       else:
         return True
   return False
     

# Remove Nth Node from end of list

from linked_list import LinkedList
from linked_list_node import LinkedListNode

def remove_nth_last_node(head, n):
  left = head
  right = head
  for i in range(n):
    right = right.next
  if not right:
    head = left.next
    return head
  while right.next:
    right = right.next
    left = left.next
  left.next = left.next.next
  return head
  



# sort colors

def sort_colors(colors):
  start = 0
  current = 0
  end = len(colors)-1
  while current <= end:
    if colors[current] == 0:
      colors[current] = colors[start]
      colors[start] = 0
      start += 1 
      current += 1 
    elif colors[current] == 1:
      current += 1
    elif colors[current] == 2:
      colors[current] = colors[end]
      colors[end] = 2
      end -= 1
  return colors
      
      

# reverse words in string



# valid word abbreviation

def valid_word_abbreviation(word, abbr):
  word_p = 0
  abbr_p = 0
  while abbr_p < len(abbr):
    if abbr[abbr_p].isdigit() and abbr[abbr_p] == '0':
      return False
    elif abbr[abbr_p].isdigit() and abbr[abbr_p] != '0':
      i = abbr_p
      s = ""
      while  i<len(abbr) and abbr[i].isdigit():
        s = s+abbr[i]
        i = i+1
      word_p += int(s)
      abbr_p = i
    elif abbr[abbr_p].isalpha():
      if word_p < len(word) and abbr[abbr_p] == word[word_p]:
        word_p += 1 
        abbr_p += 1
      else:
        return False 
  if word_p == len(word):
    return True
  else:
    return False
        
        
        
        
      
    # else:
    #   if abbr[abbr_p] == word[word_p]:
    #     abbr_p += 1
    #   else:
    #     return False
        
      
      
      
 
  # num = '0123456789'
  # for i in abbr:
  #   if i not in num:
  #     if i == word[j]:
  #       j+=1
  #     else:
  #         return False
  #   else:
  #     j+=int(i)
  # return True

    

# valid palindome II



def is_palindrome(string):
  start_p = 0 
  end_p = len(string)-1
  check = 0
  while start_p < end_p:
    if string[start_p].lower() != string[end_p].lower():
      return check_palin(string, start_p+1, end_p) or check_palin(string, start_p, end_p-1)
    start_p += 1 
    end_p -= 1
  return True
  
def check_palin(string,l,r):
  while l<r:
    if string[l].lower()  != string[r].lower():
      return False
    l += 1
    r -= 1 
  return True
      
    
    
  
          
        
  
          
