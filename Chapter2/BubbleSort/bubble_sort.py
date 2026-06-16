def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped by the inner loop, the array is sorted
        if not swapped:
            break
            
    return arr



arr = [1, 7, 3, 2, 5, 6, 4]
bubble_sort(arr)
print(arr)