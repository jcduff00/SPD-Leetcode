#Assuming we are moving zeroes to the left

def move_zeroes(nums):
    left = 0  #Step 1: Initialize the left pointer to the start of the array
    right = 0  #Step 2: Initialize the right pointer to the start of the array

    while right < len(nums):  #Step 3: Continue until the right pointer reaches the end of the array
        if nums[right] != 0:  #Step 4: If the element at the right pointer is non-zero
            nums[left], nums[right] = nums[right], nums[left]  #Step 5: Swap the non-zero element with the element at the left pointer
            left += 1  #Step 6: Move the left pointer to the next position
        right += 1  #Step 7: Move the right pointer to the next position

    while left < len(nums):  #Step 8: Fill the remaining elements with zeros
        nums[left] = 0
        left += 1

#Step 9: Implementation
nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)