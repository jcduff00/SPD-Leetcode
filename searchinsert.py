def search_insert(nums, target):
    left = 0  #Step 1: Create a left pointer that initially points to the start of the array
    right = len(nums) - 1  #Step 2: Create a right pointer initially points to the end of the array

    while left <= right:  #Step 3: Create a while loop which will continue the loop until the search range becomes empty
        mid = (left + right) // 2  #Step 4: Calculate the middle index
        
        if nums[mid] == target:
            return mid  #Step 5: Return the target if it is found at the middle index
        elif nums[mid] > target:
            right = mid - 1  #Step 6: If the target is in the left half, update the right pointer
        else:
            left = mid + 1  #Step 7: If the target is in the right half, update the left pointer
    
    return left  #Step 8: If the target not found, return the insertion point

#Step 9: Implementation
nums = [1, 3, 5, 6]
target = 5
print(search_insert(nums, target))
