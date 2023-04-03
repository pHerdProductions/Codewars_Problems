# Function to encode a string where a character encodes to '(' if it appears once and ')' if more than once
def duplicate_encode(word):
    word = word.lower() # Lowercase the string as caser doesn't matter
    
    # Create a dictionary to hold how many times a character appears
    # Could use Python's Counter from Collections
    # This is faster than using .count()
    dic = {}
    for c in word:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    
    # For every character in the string, add '(' or ')' depending on if it appears once or more
    ans = ''
    for c in word:
        ans += '(' if dic[c] == 1 else ')'
    
    # Return our encoded string!
    return ans
