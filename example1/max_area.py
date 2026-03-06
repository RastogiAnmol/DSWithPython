def container_with_most_water(arr: list[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr)-1
    max_area = 0
    while left < right:
        area = min(arr[left], arr[right]) * (right-left)
        if area > max_area:
            max_area = area
        if left >= right:
            right -= 1
        else:
            left += 1
    return max_area

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = container_with_most_water(arr)
    print(res)