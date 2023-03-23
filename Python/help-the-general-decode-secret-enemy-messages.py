# Helper function to retrieve the key from a dictionary based on the value
def getKey(val, dic):
    for key, value in dic.items():
        if val == value:
            return key

# Function to decode a message. The overall encode algorithm is (((valC * 2) * 2^i) % 67) where valC is the value of that character in the dictionary and i is the position in the string
def decode(s):
    
    # Dictionary of values based on a character
    dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
          'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52,
          '0': 53, '1': 54, '2': 55, '3': 56, '4': 57, '5': 58, '6': 59, '7': 60, '8': 61, '9': 62, '.': 63, ',': 64, '?': 65, ' ': 66, ';': 67}
    
    ans = ''    # The decoded message we will eventually return
    
    # Go through every character in the message
    for i, c in enumerate(s):
        
        # If the character is not in our dictionary, it must be one of these characters which don't get encoded: !@#$%^&*()_+-
        if c not in dic:
            ans += c
        
        # The character is in our dictionary and needs to be decoded
        else:
            cnt = 0         # Helper count variable
            valC = dic[c]   # Value of the character based on our dictionary
            
            # Repeat until we break;
            while True:
                
                # If the value is divisible by 2, divide in half and add 1 to our count
                if valC % 2 == 0:
                    valC /= 2
                    cnt += 1
                    
                # If it's not divisible by 2, add 67. This is based on the fact that there is 67 characters which get encoded
                else:
                    valC += 67
                    
                # If the cnt variable is greater than the position of the current character in the string, break out of the loop
                if cnt == i + 1:
                    break;
            
            # We can now retrieve the character based on the value and add it to our final string
            ans += getKey(valC, dic)
        
    # Return the decoded string
    return ans;
