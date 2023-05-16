def is_palindrome(x):
    #Step 1: Convert the integer to a string
    str_x = str(x)

    #Step 2: Reverse the string using string slicing
    reversed_str = str_x[::-1]

    #Step 3: Compare the original string with the reversed string
    if str_x == reversed_str:
        return True 
    else:
        return False
    
#Step 4: Implementation
print(is_palindrome(121))