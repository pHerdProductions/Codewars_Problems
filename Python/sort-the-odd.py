# Function to, for the array/list, sort the odd numbers, keeping the positions of the even numbers
def sort_array(arr):
  
  # If the given array is empty, we can simply return an empty array
  if not arr: return []

  odds = [] # Variable to hold the list of odd numbers
  pos = []  # Variable to hold the list of indices where odd numbers are found
  
  # Iterating through the array
  for i, n in enumerate(arr):
    
    # If the number is odd
    if n % 2 == 1:
      
      # Append the number to our 'odds' array, and insert the index number into our 'pos' array (so we don't have to call reverse() later)
      odds.append(n)
      pos.insert(0, i)

  odds.sort(reverse=True) # Sort the array of odd numbers from largest to smallest. We do this because, like 'pos' array, we will be using .pop()

  # Iterate for the length of the initial array
  for i in range(len(arr)):
    
    # If 'pos' is not empty and the last element is equal to i (our current position in the array)
    if pos and i == pos[-1]:
      
      # Change that value to the last value of odds with pop() (which is the smallest number). Also pop() the last element out of 'pos'
      arr[i] = odds.pop()
      pos.pop()
      
      # If our 'pos' array is empty, break out of the loop. Could use 'odds' variable too
      if not pos: break

  # Return the new array!
  return arr
