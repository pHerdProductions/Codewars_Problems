def bouncing_ball(h, bounce, window):
    
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h: return -1
    
    ans = 0
    while h > window:
        ans += 1
        h *= bounce
        if h > window: ans += 1
    return ans
