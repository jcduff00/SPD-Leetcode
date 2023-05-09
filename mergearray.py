def merge(nums1, m, nums2, n):
    # Step 1: Initialize three pointers:
    # p1: points to the last non-zero element in nums1
    # p2: points to the last element in nums2
    # p: points to the last position of the merged array
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    # Step 2: Compare elements at nums1[p1] and nums2[p2] while both pointers are valid
    while p1 >= 0 and p2 >= 0:
        # Step 3: If the current element in nums1 is greater than the current element in nums2, assign the element from nums1 to the merged array at position p
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            # Step 4: Decrement p1 and p by 1 to move to the next elements
            p1 -= 1
        else:
            # Step 5: If the current element in nums1 is less than or equal to the current element in nums2
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # Step 6: Copy any remaining elements from nums2 to the beginning of nums1
    nums1[:p2 + 1] = nums2[:p2 + 1]

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]