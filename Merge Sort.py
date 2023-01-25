def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid_array = len(arr) // 2
    left = arr[:mid_array]  # From the start to the mid of array
    right = arr[mid_array:]  # From the mid of array to the end

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_list(left, right, arr)



def merge_two_sorted_list(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    # i and j are two lists' indexes while k is the original sorted list
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


nums = [70, 1, 32, 61, 11, 8, 3, 53, 69, 14]
merge_sort(nums)
print(nums)
