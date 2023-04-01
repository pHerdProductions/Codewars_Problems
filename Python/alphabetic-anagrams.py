import math # Import math for factorial calculations

# Function to calculate the amount of possibilities changing the current letter (if there are letters later in the string that come sooner in the alphabet)
def calcIndex(word):
    l = len(word) # Amount of letters
    
    # For permuation calculations, we do the factorial of the amount of elements (which would be the total permutations if they are all unique)
    top = math.factorial(l)
    
    # Create a dictionary to hold each letter and the amount of times it appears
    chars = {}
    for c in word:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    
    # Calculate the second part to the permutation calculation which accounts for similar elements
    bot = 1
    for c in chars:
        bot *= math.factorial(chars[c])
    
    # Now that we have both parts to the permutation calculation, we simply divide and we get the total possible permutations given the string of letters
    possible = top//bot
    
    # Now we convert our dictionary to a list(array) and sort it alphabetically
    letters = list(zip(chars.keys(), chars.values()))
    letters.sort()
    
    curLetter = word[0] # Current letter we are calculating for
    
    earlier = 0 # The amount of letters that come after the current letter in the string that would come sooner in the alphabet
    
    # Going through our list that is sorted, we add up the total letters coming later in the string that come sooner in the alphabet
    i = 0
    while letters[i][0] != curLetter:
        earlier += letters[i][1]
        i += 1
    
    # Now we can return the total possibilities that would come sooner in the alphabetical index given the current letter,
    # being index 0, which we iterate through in our main function
    return int(possible/l) * earlier

def listPosition(word):
    if len(word) == 1: return 1 # If there is only one letter then we know there is only one possible permutation

    # For each letter, beginning to end, calculate and add to the total (which starts at 1 which would mean the string is already in alphabetical order)
    ans = 1
    for i in range(len(word)):
        ans += calcIndex(word[i:])  # We send the string to our calcIndex() function which goes from the current letter to the end
        
    # Return the alphabetical index of the string!
    return ans
