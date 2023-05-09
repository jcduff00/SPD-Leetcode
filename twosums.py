def twoSum(nums, target):
    # Step 1: initialize empty hash map
    hashMap = {}

    # Step 2: create index variable and iterate through the list
    for index, num in enumerate(nums):
        # Step 3: create calculation for the complement given each number in the list
        complement = target - num

        # Step 4: conditional to assess whether the given complement is present in the list
        if complement in hashMap:
            return [index, hashMap[complement]]

        # Step 5: add number to the hash map if the complement does not exist
        hashMap[num] = index

    # Step 6: if no numbers exist, spit out value error to signify the empty hash map
    raise ValueError("No two numbers add up to the target.")

nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]