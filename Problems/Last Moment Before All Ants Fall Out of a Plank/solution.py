import io
from typing import List
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans=0
        for i in left:
            ans=max(i,ans)
        for i in right:
            ans=max(n-i,ans)
        return ans

obj = Solution()
#data = obj.getLastMoment(n = 4, left = [4,3], right = [0,1])
#data = obj.getLastMoment(n = 7, left = [], right = [0,1,2,3,4,5,6,7])
data = obj.getLastMoment(n = 7, left = [0,1,2,3,4,5,6,7], right = [])
print(data)