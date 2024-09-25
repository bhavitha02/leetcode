# happy number



from sum_of_squared_digits import sum_of_squared_digits

def is_happy_number(n):
  if n == 1:
    return True
  slow_pointer = n
  fast_pointer = sum_of_squared_digits(n)
  while slow_pointer != fast_pointer:
    if fast_pointer == 1:
      return True
    slow_pointer = sum_of_squared_digits(slow_pointer)
    fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))
    
  return False 
  # if n ==1 :
  #   return True

  #   # Replace this placeholder return statement with your code
  # slow = n 
  # fast = sum_of_squared_digits(n)

  # while slow!=fast:
  #   if fast == 1:
  #     return True # happy number
  #   slow = sum_of_squared_digits(slow)
  #   fast = sum_of_squared_digits(sum_of_squared_digits(fast))

    
  # return False


  
    


#   linked list cycle


from linked_list import LinkedList

def detect_cycle(head):
  if head is None:
        return False
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False
    
    

   


