# The above solution using a flexible sliding window uses O(n) time complexity. 
# As a follow up, is there an algorithm that solves this question in O(n log(n))? 
# Yes! Consider using the n elements in nums as a starting point of a subarray, 
# and then use O(log(n)) time complexity to find the endpoint of that subarray. 
# This is can be done via a for loop and a binary search on a prefix sum array.

def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    prefix_sum = [0]
    for n in nums:
        prefix_sum.append(prefix_sum[-1] + n)

    size = len(nums)+1
    for start in range(len(nums)):
        total = 0
        l, r, end = 0, len(nums)-1, -1
        while l <= r:
            mid = (l+r)//2
            if prefix_sum[mid+1] - prefix_sum[start] >= target:
                end, r = mid, mid - 1
            else: l = mid + 1
        if end != -1: size = min(size, end-start+1)
    return size if size != len(nums)+1 else 0