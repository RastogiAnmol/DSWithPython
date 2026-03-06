def subarray_sum_shortest(nums: list[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = current_length = current_sum = 0
    min_length = int(1e9)
    for right in range(len(nums)):
        current_length += 1
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, current_length)
            current_sum -= nums[left]
            current_length -= 1
            left += 1
            
    return min_length

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_shortest(nums, target)
    print(res)
