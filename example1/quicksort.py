def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# Example usage:
if __name__ == "__main__":
    sample_array = [34, 7, 23, 32, 5, 62]
    sorted_array = quicksort(sample_array)
    print("Sorted array:", sorted_array)