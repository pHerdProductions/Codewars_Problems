# Function to find the index of an array where the sum of all elements to the left equals the sum of all elements to the right
def find_even_index(arr):
  
  # Iterate through all elements in the array
  for i in range(len(arr)):
    
    # If the sum of the elements to the left of the index is equal to the sum of all elements to the right
    if sum(arr[:i]) == sum(arr[i+1:]):
      
      return i # Found the index, return it
    
  # If we made it here, there is no such index, and we simply return -1
  return -1
