# Helper function to find the index of the largest number coming after the number we're checking for
def check(nums):
  
  ret = -1  # Variable for the index we will return. -1 means none found
  cur = '-1'  # Current largest number less than what we're checking on
  num = nums[0] # Number we're checking on
  
  # Iterate through each number, starting after the first digit
  for i in range(1, len(nums)):
    
    # If the number we're checking for is greater than the number we're testing against
    # AND the number we're testing against is greater than our current largest number
    if num > nums[i] and nums[i] > cur:
      
      # Then we set cur to that number and set ret to the index
      cur = nums[i]
      ret = i
      
  return ret  # Return -1 if we didn't find one, or the index if we did

# Main function that will return the next smallest number, with the same digits
def next_smaller(n):
  
  # Seperate the digits into a list/array. NOTE: coded solution with converting them to ints, but string comparisons works just fine
  nums = list(str(n))

  # If the numbers are all in order, we know its the smallest number with those digits already and we can return -1
  if nums == sorted(nums): return -1

  # Iterate front to back starting with the second to last number
  for i in range(len(nums)-2, -1, -1):
    
    # Check the numbers from i to the end, and set what our helper function check() returns to j
    j = check(nums[i:])

    # If check() returns -1 we know there's no way to make a smaller number yet, so keep searching, moving to the left
    # AND we make sure the number we're moving, if we'd be moving it to the very beginning, isn't 0, which checks for the leading zero edge case
    if j != -1 and not (nums[i+j] == '0' and i == 0):
      
      # If we passed those checks, pop that number and insert it to the index of the number we we're testing in our check() function
      nums.insert(i, nums.pop(i+j))
      
      # Take the numbers from the beginning to the index of the number we just moved and
      # add the rest of the numbers which we sort in reverse order (make those numbers largest-smallest)
      nums = nums[:i+1] + sorted(nums[i+1:], reverse = True)
      
      # Now that we have the answer, it's still in list form. So we join them together, and since they are currently strings, convert it to an Int
      return int(''.join(nums))

  # If we made it here, it means the digits are currently in order for the smallest number possible
  # This exists for the leading zero edge case scenario
  return -1
