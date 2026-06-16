def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    

# Example usage:
arr = [7, 2, 1, 6, 8, 5, 3, 4]
result = quicksort(arr)
print(result)