#This is a rather simple one. 
#Step 1: Create a function that will determine the anagram length
def is_anagram(s, t):
    if len(s) != len(t):
        #Step 2: The if statement will only allow the function to proceed if the character length of string s and string t are the same number.
        return False
#Step 3: The function will return sorted forms of s and t to determine if the character patterns are the same
    return sorted(s) == sorted(t)

#Step 4: Implementation
print(is_anagram("rat", "cat"))