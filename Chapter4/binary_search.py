def binary_search(arr, target):
    def helper(low, high):
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid + 1, high)
        else:
            return helper(low, mid-1)
        return -1
    return helper(0, len(arr) - 1)

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 4
result = binary_search(arr, target)
if result != -1:    print(f"Element found at index: {result}")
else:    print("Element not found in the array.")

    