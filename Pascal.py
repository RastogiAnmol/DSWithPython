from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev_row = self.getRow(rowIndex-1)
        return [1] + [prev_row[i] + prev_row[i+1] for i in range(len(prev_row)-1)] + [1]

obj = Solution()
r = obj.getRow(5)
print(r)