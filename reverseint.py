def reverse(x):
    #Step 1: Define the integer limits
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    #Step 2: Flag to indicate if x is negative
    is_negative = False
    if x < 0:
        is_negative = True
        x = -x
    
    #Step 3: Initialize the result variable
    result = 0
    
    #Step 4: Create a while loop that will continue as long as x is greater than 0
    while x > 0:
        digit = x % 10
        
        #Step 5: Check if reversing x would cause an overflow
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
            return 0
        
        #Step 6: Append the digit to the result by multiplying the integer by 10 and adding it to the result
        result = result * 10 + digit
        
        #Step 6: Remove the last digit from x by dividing the integer by 10
        x //= 10
    
    #Step 7: Apply the sign to the result
    if is_negative:
        result = -result
    
    Step 8: Implementation
    return result