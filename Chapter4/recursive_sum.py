def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

# Example usage:
numbers = [64, 25, 12, 22, 11]
result = sum(numbers)
print("Sum of array:", result)