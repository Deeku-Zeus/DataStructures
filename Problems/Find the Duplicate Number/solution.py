import io
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break

        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow 

obj = Solution()
#data = obj.findDuplicate(nums = [1,3,4,2,2])
data = obj.findDuplicate(nums = [3,1,3,4,2])
print(data)