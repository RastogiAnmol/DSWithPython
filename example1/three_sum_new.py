def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    for i in range(len(nums)):
        if nums[i] > 0 or i > 0 and nums[i] == nums[i-1]: continue
        l, r = i+1, len(nums)-1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                res.append([nums[i], nums[l], nums[r]])
                l, r = l+1, r-1
                while l < len(nums) -1 and nums[l] == nums[l-1]:
                    l += 1
            elif total > 0:
                r -= 1
            else:
                l += 1
    return res

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = threeSum(nums)
    for row in res:
        print(" ".join(map(str, row)))