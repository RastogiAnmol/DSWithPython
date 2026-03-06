def minimum_difference_pairs(arr: list[int]) -> list[list[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    if len(arr) < 2:
        return []
    sorted_array = sorted(arr)
    least_diff = sorted_array[1] - sorted_array[0]
    for i in range(2, len(sorted_array)):
        if sorted_array[i] - sorted_array[i-1] < least_diff:
            least_diff = sorted_array[i] - sorted_array[i-1]
    result = []
    for i in range(len(sorted_array)-1):
        if sorted_array[i+1] - sorted_array[i] == least_diff:
            result.append([sorted_array[i], sorted_array[i+1]])
    return result

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = minimum_difference_pairs(arr)
    for row in res:
        print(" ".join(map(str, row)))
