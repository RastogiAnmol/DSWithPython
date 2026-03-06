def relative_sort_array(arr1: list[int], arr2: list[int]) -> list[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    index = {val: i for i, val in enumerate(arr2)}
    result = sorted(arr1, key=lambda x: (index.get(x, len(arr2)), x))
    return result

if __name__ == "__main__":
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    res = relative_sort_array(arr1, arr2)
    print(" ".join(map(str, res)))