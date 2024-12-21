import io
from typing import List
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            j = nums.index(min(nums))
            nums[j]*=multiplier
        return nums

obj = Solution()
#data = obj.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2)
data = obj.getFinalState(nums = [1,2], k = 3, multiplier = 4)
print(data)