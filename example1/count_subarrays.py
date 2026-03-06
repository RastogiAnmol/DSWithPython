def subarray_sum_total(arr: list[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    from collections import Counter
    prefix_sum: Counter[int] = Counter()
    prefix_sum[0] = 1
    cur_sum = count = 0
    for right in range(len(arr)):
        cur_sum += arr[right]
        complement = cur_sum - target
        if complement in prefix_sum:
            count += prefix_sum[complement]
        prefix_sum[cur_sum] = prefix_sum[cur_sum] + 1
    return count

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_total(arr, target)
    print(res)
