from typing import List


def quick_sort(arr: List[int], start: int, end: int) -> None:
    """
    Recursively sorts an array in-place using the QuickSort algorithm.
    
    :param arr: The array to be sorted.
    :param start: The starting index of the sub-array.
    :param end: The ending index of the sub-array.
    """
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi - 1)
        quick_sort(arr, pi + 1, end)


def partition(arr: List[int], start: int, end: int) -> int:
    """
    Partitions the sub-array by choosing the last element as a pivot,
    placing smaller elements to its left and larger to its right.
    
    :param arr: The array being partitioned.
    :param start: The starting index of the partition segment.
    :param end: The ending index (and pivot) of the partition segment.
    :return: The final sorted index of the pivot element.
    """
    pivot = arr[end]
    pi = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pi] = arr[pi], arr[i]
            pi += 1
    # Swap with pivot in order to place pivot at right index
    arr[pi], arr[end] = arr[end], arr[pi]
    return pi



# Driver Code


arr = [7, 2, 1, 6, 8, 5, 3, 4]
quick_sort(arr, 0, len(arr)-1)
print(arr)