def sort(nums):
    for i in range(9):
        minpos = i
        for j in range(i, 10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = [70, 1, 32, 61, 11, 8, 3, 53, 69, 14]