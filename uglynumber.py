def ugly_num(n):
    #Step 1: Create a conditional which assesses whether n is greater than 0, as negative numbers and zeroes cannot be ugly numbers
    if n <= 0:  
        return False  

    while n % 2 == 0:
        n //= 2  #Step 2: Divide n by 2 as long as it is divisible by 2

    while n % 3 == 0:
        n //= 3  #Step 3: Divide n by 3 as long as it is divisible by 3

    while n % 5 == 0:
        n //= 5  #Step 4: Divide n by 5 as long as it is divisible by 5

    return n == 1  #Step 5: Determine whether n becomes 1, as if it does, it is an ugly number (only has prime factors 2, 3, and 5)

#Step 6: Implementation
print(ugly_num(6))