import re # Import RegExp

# Function to count how many smiley faces there are in the given array based on certain characteristics that constitute one
def count_smileys(arr):
    
  ans = 0 # Total number of smiley faces

  # Iterate through each element (string) in the array
  for s in arr:

    # If the element matches our RegExp, it constitutes a smiley face, and add one to our variable 'ans'
    if re.match('[:;][-~]?[)D]', s):
      ans += 1
      
  # Return the total amount of smileys!
  return ans
