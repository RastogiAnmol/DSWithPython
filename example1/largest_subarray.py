def subarray_sum_fixed(nums: list[int], k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    i, j = 0, k
    current_sum, largest = 0, 0
    for index in range(k):
        current_sum += nums[index]
    largest = current_sum
    while j < len(nums):
        current_sum = current_sum + nums[j] - nums[i]
        largest = max(current_sum, largest)
        j += 1
        i += 1
    return largest

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = subarray_sum_fixed(nums, k)
    print(res)
