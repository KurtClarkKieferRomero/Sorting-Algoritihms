def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(nums, start, end):
    pivot_index = start
    pivot = nums[pivot_index]

    while start < end:
        while start < len(nums) and nums[start] <= pivot:
            start = start + 1

        while nums[end] > pivot:
            end = end - 1

        if start < end:
            swap(start, end, nums)

    swap(pivot_index, end, nums)
    return end


# create a quick sort function
def quick_sort(nums, start, end):
    if start < end:
        part_ind = partition(nums, start, end)  # Will store partition index
        quick_sort(nums, start, part_ind - 1)   # Will sort left partition
        quick_sort(nums, part_ind + 1, end)     # Will sort right partition



nums = [70, 1, 32, 61, 11, 8, 3, 53, 69, 14]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
