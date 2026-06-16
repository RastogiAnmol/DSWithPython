from pprint import pprint

def selection_sort(arr):
    def helper(low, high):
        smallest = arr[low]
        smallest_index = low
        for i in range(low+1, high):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest_index
    
    for i in range(len(arr)):
        smallest_index = helper(i, len(arr))
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

# Example usage:
arr = [23, 87, 42, 5, 66, 91, 14, 73, 38, 59, 12, 99, 31, 50, 8, 84, 47, 61, 19, 95]
result = selection_sort(arr)
pprint(result, compact=True)