# Function to find k where n*k == a^p + b^(p+1) + c^(p+2)... ex: n = 89, p = 1: 89 * k == 8^1 + 9^2 == 89 | k == 1
def dig_pow(n, p):
    
    # Iterating through the digits, create a variable for the sum of all digits^(p + i)
    total = sum( int(x) ** (p + i) for i, x in enumerate(str(n)) )
    
    # Return total divided by n if they are divisible (without a remainder), else return -1 (no such k)
    return total//n if total%n == 0 else -1
