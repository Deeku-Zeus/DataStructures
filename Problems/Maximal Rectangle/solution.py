import io
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n=len(matrix)
        m=len(matrix[0])
        height=[0]*(m+1)
        ans=0
        for r in matrix:
            for i in range(m):
                
                height[i]=height[i]+1 if r[i]=='1' else 0
            stack=[-1]
            for i in range(m+1):
                while height[i]<height[stack[-1]]:
                    h=height[stack.pop()]
                    w=i-stack[-1]-1
                    ans=max(ans,h*w)
                stack.append(i)
        return ans

obj = Solution()
#data = obj.maximalRectangle(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
#data = obj.maximalRectangle(matrix = [["0"]])
data = obj.maximalRectangle(matrix = [["1"]])
print(data)