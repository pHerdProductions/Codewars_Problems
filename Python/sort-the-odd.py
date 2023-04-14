# Function to, for the array/list, sort the odd numbers, keeping the positions of the even numbers
def sort_array(arr):
  
  # Create an array for every odd number in the given arr, and sort from largest to smallest
  odds = sorted((x for x in arr if x%2 != 0), reverse = True)
  
  # Return an array where, iterating through arr, we keep the evens in place, but if it's odd, pop() from our sorted 'odds' array instead
  return [x if x%2 == 0 else odds.pop() for x in arr]
