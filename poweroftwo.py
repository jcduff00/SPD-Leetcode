def isPowerOfTwo(n):
    #Step 1: Check if n is less than or equal to zero
    if n <= 0:
        return False
    
    #Step 2: Count the number of set bits in n
    count = 0
    while n > 0:
        if n & 1:
            count += 1
        n >>= 1
    
    #Step 3: If there is only one set bit, n is a power of two
    return count == 1