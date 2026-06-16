def merge_sort(arr, n):
    if n < 2:
        return
    mid = n // 2
    l = arr[:mid]
    r = arr[mid:]
    merge_sort(l, mid)
    merge_sort(r, n - mid)
    merge(l, r, arr, mid, n - mid)


def merge(l, r, arr, left_count, right_count):
    i = j = k = 0
    while i < left_count and j < right_count:
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    while i < left_count:
        arr[k] = l[i]
        i += 1
        k += 1
    while j < right_count:
        arr[k] = r[j]
        j += 1
        k += 1


# Driver Code


arr = [1, 7, 3, 2, 5, 6, 4, 10, 8, 9]
merge_sort(arr, 10)
print(arr)