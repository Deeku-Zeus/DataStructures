import io
from typing import List
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bannedSet = set(banned)
        curSum = 0 
        count = 0 
        for i in range(1,n+1): 

            if i in bannedSet:
                continue
            else:
                curSum +=i
                
            if curSum <= maxSum:
                count+=1
            else:
                return count
        return count

obj = Solution()
#data = obj.maxCount(banned = [1,6,5], n = 5, maxSum = 6)
#data = obj.maxCount(banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1)
data = obj.maxCount(banned = [11], n = 7, maxSum = 50)
print(data)