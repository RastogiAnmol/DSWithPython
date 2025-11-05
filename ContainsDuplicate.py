# pylint: skip-file

from ast import List

class Solution:
    def containsDuplicate(self, nums) -> bool:
        cache = {}
        for item in nums:
            if item in cache:
                return True
            cache[item] = True
        return False
    
ab = Solution()
print(ab.containsDuplicate([1,2,3,1]))  # True
print(ab.containsDuplicate([1,2,3,4]))  # False
print(ab.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # True