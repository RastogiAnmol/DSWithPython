def partition(arr, low, high):
    # Choose the last element as pivot
    pivot = arr[high]
    pi = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[pi], arr[j] = arr[j], arr[pi]  # swap
            pi += 1

    # Place pivot in correct position
    arr[pi], arr[high] = arr[high], arr[pi]
    return pi


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


# Example usage
if __name__ == "__main__":
    numbers = [34, 7, 23, 32, 5, 62]
    print("Original array:", numbers)

    quicksort(numbers, 0, len(numbers) - 1)

    print("Sorted array:", numbers)
