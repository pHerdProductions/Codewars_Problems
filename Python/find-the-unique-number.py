def find_uniq(arr):
    num1 = arr[0]
    num2 = arr[1]
    
    if num1 == num2:
        for n in arr[2:]:
            if n != num1:
                return n
            
    else:
        return num1 if arr[2] == num2 else num2
