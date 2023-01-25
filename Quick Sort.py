# create a swapping technique for the start and end
def swap(a, b, arr):
    if a != b:  # if the arr has the same element, don't switch
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


# create a partition function to make the pivot in the middle
def partition(nums):
    pivot_index = 0  # Pivot is the start value
    pivot = nums[pivot_index]

    # Create a start and end locator
    start = pivot_index + 1
    end = len(nums) - 1

    while start < end:  # If the start and end cross each other, this will stop
        # Create a way to move the start and end index
        while nums[start] <= pivot:
            start = start + 1  # This will move the start forward until it finds number less than pivot

        while nums[end] > pivot:
            end = end - 1  # This will move the end backward until it finds number greater than pivot

        if start < end:  # This will make it safe
            swap(start, end, nums)

    swap(pivot_index, end, nums)  # This will make it so that the pivot is in the sorted order


# create a quick sort function
def quick_sort(nums):
    partition(nums)


if __name__ == '__main__':
    nums = [70, 1, 32, 61, 11, 8, 3, 53, 69, 14]
    quick_sort(nums)
    print(nums)
