import io
from typing import List
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        ans=0
        for r in range(1,row):
            for c in range(col):
                matrix[r][c]+=matrix[r-1][c] if matrix[r][c] else 0

        for r in range(row):
            matrix[r].sort(reverse=True)
            for c in range(col):
                ans=max(ans,(c+1)*matrix[r][c])
        return ans 

obj = Solution()
#data = obj.largestSubmatrix(matrix = [[0,0,1],[1,1,1],[1,0,1]])
#data = obj.largestSubmatrix(matrix = [[1,0,1,0,1]])
data = obj.largestSubmatrix(matrix = [[1,1,0],[1,0,1]])
print(data)