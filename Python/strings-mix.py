import re # Import to use regular expressions

# Function to visualize how different two strings are, outputting a string
def mix(s1, s2):
    
    # Clean up both strings by getting rid of any character that is not a lowercase alphabetic character
    s1 = re.sub('[^a-z]', '', s1)
    s2 = re.sub('[^a-z]', '', s2)
    
    counts = [] # An array to hold data that we will sort
    
    # For every character in the lowercase alphabet
    for c in 'abcdefghijklmnopqrstuvwxyz':
        
        # Two variables holding how many of a character is in each string
        c1 = s1.count(c)
        c2 = s2.count(c)
        
        # We're only looking for characters where there is greater than 1 in either of the strings
        if c1 > 1 or c2 > 1:
        
            # Based on whether the strings have a different amount of the character or equal
            # The first value in the array we append to 'counts' is the amount of times that char appeared in the string(s), and will be used to sort
            # The second value is only used to sort where we prioritize the first string, second string, then if they equal
            # The third value is the string for that specific char that will be added to our final output string
            if c1 > c2:
                counts.append([c1, 2, f'1:{c*c1}'])
            elif c1 < c2:
                counts.append([c2, 1, f'2:{c*c2}'])
            else:
                counts.append([c1, 0, f'=:{c*c1}'])
            
    # Sort first by the count of a specific character, greatest first, then by which string the count was in or if they were equal
    counts = sorted(counts, key = lambda x: (x[0], x[1]), reverse = True)
    
    # We return the strings in our counts array, which have been sorted, by joining them with the '/' character
    return '/'.join(x[2] for x in counts)
