def merge_two_sorted_list(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    # i and j are two lists' indexes while k is the original sorted list
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = arr[i]
            i += 1
        else:
            arr[k] = arr[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = arr[a]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = arr[j]
        j += 1
        k += 1



nums = [70, 1, 32, 61, 11, 8, 3, 53, 69, 14]