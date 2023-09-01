import io
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]
        for i in range(1,n+1):
            if i%2==1:
                dp.append(dp[i-1]+1)
            else:
                dp.append(dp[i//2])
        return dp 

obj = Solution()
#data = obj.countBits(n = 2)
data = obj.countBits(n = 5)
print(data)