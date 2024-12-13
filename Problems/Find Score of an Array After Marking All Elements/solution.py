import io
from typing import List
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n, j, s = len(nums), 0, 0
        while j < n:
            odd = even = 0
            while j + 1 < n and nums[j] > nums[j + 1]:
                if j & 1: odd += nums[j]
                else: even += nums[j]
                j += 1
            s += (odd if j & 1 else even) + nums[j]
            j += 2
        return s

obj = Solution()
#data = obj.findScore(nums = [2,1,3,4,5,2])
data = obj.findScore(nums = [2,3,5,1,3,2])
print(data)