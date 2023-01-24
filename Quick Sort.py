def quick_sort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    else:
        pivot = nums.pop()


nums = [70, 1, 32, 61, 11, 8, 3, 53, 69, 14]