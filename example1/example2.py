def remove_duplicates(arr: list[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    slow_ptr, fast_ptr = 0, 0
    while fast_ptr  < len(arr):
        if arr[slow_ptr] == arr[fast_ptr]:
            fast_ptr += 1
        else:
            slow_ptr += 1
            arr[slow_ptr] = arr[fast_ptr]
    return slow_ptr

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = remove_duplicates(arr)
    print(" ".join(map(str, arr[:res])))