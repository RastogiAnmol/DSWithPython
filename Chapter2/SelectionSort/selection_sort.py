def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Assume the current position has the minimum
        min_index = i
        
        # Find the index of the minimum element in the remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# Example usage:
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print("Sorted array:", sorted_numbers)