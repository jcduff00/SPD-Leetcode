def add_digits(num):
    while num > 9:  #Step 1: Continue until the number becomes a single digit
        num = sum(int(digit) for digit in str(num))  #Step 2: Calculate the sum of digits by converting the number to a string and summing the integers
    return num  #Step 3: Return the single-digit result

#Step 4: Implementation
print(add_digits(38))