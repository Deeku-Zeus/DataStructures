import io
from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        pass

obj = Solution()
#data = obj.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70])
#data = obj.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60])
data = obj.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4])
print(data)