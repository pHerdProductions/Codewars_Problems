import numpy as np      # Import NumPy for easier array slicing

# Function to create a 2D array spiral (1's being the spiral, 0's being empty space)
def spiralize(size):
    grid = np.array([[0]*size]*size)    # Create a 2D NumPy array
    
    l, r, t, b = 0, size - 1, 0, size - 1   # Left, Right, Top, Bottom indices
    
    while(l <= r or t <= b):    # While our outer indices still have room to spiral
        
        # Changes 0's to 1's
        grid[t, l-(1 if l > 0 else 0):r+1] = 1  #RIGHT
        grid[t+1:b+1, r] = 1                    #DOWN
        
        # If the spiral goes down only one space, we are done
        if t == b - 1:
            break;
            
        grid[b, l:r] = 1                        #LEFT
        grid[t+2:b, l] = 1                      #UP
        
        # Move the indices two spaces inward
        t += 2
        b -= 2
        r -= 2
        l += 2
        
    return grid.tolist()    # Can't return a numpy.array type so convert to a normal Python list
