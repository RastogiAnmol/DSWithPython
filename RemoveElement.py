from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = len(nums)-1, len(nums)-1
        while i>=0:
            if nums[i] == val:
                nums[i], nums[k] = nums[k], nums[i]
                k-=1
            i-=1
        return k+1


obj = Solution()
some = [0,1,2,2,3,0,4,2]
result = obj.removeElement(some, 2)
print(result)
print(some)