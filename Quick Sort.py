def quick_sort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    else:
        pivot = nums.pop()

    elements_greater = []
    elements_lower = []

    for i in nums:
        if i > pivot:
            elements_greater.append(nums)
        else:
            elements_lower.append(nums)


nums = [70, 1, 32, 61, 11, 8, 3, 53, 69, 14]
