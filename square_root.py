#Step 1: First, we define our function
def sqrt(x):
    if x < 2:
        return x  #Step 2: Return x if it is 0 or 1

    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2  #Step 3: Calculate the middle element
        square = mid * mid  #Step 4: Calculate the square of mid

        if square == x:
            return mid  #Step 5: Return mid if its square is equal to x
        elif square > x:
            right = mid - 1  #Search in the left half
        else:
            left = mid + 1  #Search in the right half

    return right  #Step 6: Return the square root of x, rounded down to the nearest

#Step 7: Implementation
print(sqrt(4))