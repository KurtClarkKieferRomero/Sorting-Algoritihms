def insertion_sort(nums):
    for i in range(1, len(nums)):
        value = nums[i]
        j = i - 1
        while j >= 0 and (value < nums[j]):
            nums[j + 1] = nums[j]
            nums[j] = value
            j = j - 1
        print(nums)




nums = [70, 1, 32, 61, 11, 8, 3, 53, 69, 14]
insertion_sort(nums)
print(nums)