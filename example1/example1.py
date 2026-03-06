def singleNonDuplicate(nums):
    def to_the_left(idx):
        if (idx == len(nums)-1):
            return True
        elif (idx % 2):   # odd
            return nums[idx] != nums[idx-1]
        else:             # even
            return nums[idx] != nums[idx+1]

    left, right, ans = 0, len(nums)-1, -1
    while left <= right:
        mid = (left + right) // 2
        if to_the_left(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

nums = [0,0,1,1,2,3,3,4,4,8,8]
solution = singleNonDuplicate(nums)
print(solution)  # Output: 2