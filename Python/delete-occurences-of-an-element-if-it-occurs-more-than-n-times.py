# Function that returns a new list after deleting any elements after they appeared max_e times
def delete_nth(order, max_e):
  
  dic = {}  #  Dictionary to hold elements and times appeared
  ans = []  # New list that we will append to and eventually return

  # Iterate through each number in 'order'
  for num in order:

    # Variable 'n' equals the amount of times that element 'num' has appeared, 0 is default (not in dictionary)
    n = dic.get(num, 0)
    
    # If the element has appeared less than 'max_e' times
    if n < max_e:
      
      # Add one to the elements value by key, and append the element 'num' to the new list
      dic[num] = n + 1
      ans.append(num)

  # Return our new list!
  return ans
