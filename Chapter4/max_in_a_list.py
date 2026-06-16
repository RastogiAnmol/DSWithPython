def find_max(lst):
    if lst == []:
        return 0
    return max(lst[0], find_max(lst[1:]))

# Example usage:
numbers = [64, 25, 12, 88,  22, 11]
result = find_max(numbers)
print("Max of array:", result)