from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> str:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 0:
            return ""
        result = s[-1] + self.reverseString(s[:-1])
        return result

obj = Solution()
some = ["h","e","l","l","o"]
r = obj.reverseString(some)
print(r)