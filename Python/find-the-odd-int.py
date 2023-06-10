# Function to find the integer that appears an odd number of times given an array of ints
# There will be only one that appears an odd amount of times
def find_it(seq):
    
    # Create a dictionary to hold unique integers and the # of times they appear
    dic = {}
    for n in seq:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    
    # Iterate through each element (int) in the dictionary until we find one that the value is odd
    for d in dic:
        if dic[d] % 2 == 1:
            return d    # Then we simply return that integer. Since we know there WILL be one, we don't need an edge case return outside of this loop
