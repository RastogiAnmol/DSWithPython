def count_items(lst):
    if lst == []:
        return 0
    return 1 + count_items(lst[1:])

# Example usage:
numbers = [64, 25, 12, 22, 11]
result = count_items(numbers)
print("Length of array:", result)