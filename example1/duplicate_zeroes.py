def duplicateZeros(arr: list[int]):
    """
    Do not return anything, modify arr in-place instead.
    """
    zeroes = arr.count(0)
    n = len(arr)
    for i in range(n-1, -1, -1):
        if i + zeroes < n:
            arr[i + zeroes] = arr[i]
        if arr[i] == 0:
            zeroes -= 1
            if i + zeroes < n:
                arr[i + zeroes] = 0
arr = [1,0,2,3,0,4]
duplicateZeros(arr)
print(arr)