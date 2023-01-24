def bubble_sort(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            temp = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = temp



nums = [70, 1, 32, 61, 11, 8, 3, 53, 69, 14]
bubble_sort(nums)
print(nums)