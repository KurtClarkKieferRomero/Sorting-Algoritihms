def insertion_sort(nums):
    for i in range(1, len(nums)):
        value = nums[i]
        j = i - 1
        while j >= 0 and (value < nums[i]):




nums = [70, 1, 32, 61, 11, 8, 3, 53, 69, 14]
insertion_sort(nums)