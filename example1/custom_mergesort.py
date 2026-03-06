def compare(a, b):
    ab = a + b
    ba = b + a
    print(f"Comparing {a} and {b}: {ab} vs {ba} -> {'a before b' if ab > ba else 'b before a'}")

    # Return True if a should come before b
    return ab > ba


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# ------------------ TEST ------------------
nums = [3, 30, 34, 5, 9]
nums_str = list(map(str, nums))

sorted_nums = merge_sort(nums_str)
print("Sorted order:", sorted_nums)

largest_number = "".join(sorted_nums)
print("Largest number:", largest_number)
