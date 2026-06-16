from pprint import pprint

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


# Example usage:
arr = [23, 87, 42, 5, 66, 91, 14, 73, 38, 59, 12, 99, 31, 50, 8, 84, 47, 61, 19, 95]
result = selection_sort(arr)
pprint(result, compact=True)