def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

        print(nums)

nums = [70, 1, 32, 61, 11, 8, 3, 53, 69, 14]
bubble_sort(nums)
print(nums)