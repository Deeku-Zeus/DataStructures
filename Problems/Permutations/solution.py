import io
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        arr = []

        def backtrack(index):
            if(index == n):
                arr.append(nums[:])
                return
            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index] # swap
                backtrack(index + 1)
                nums[index], nums[i] = nums[i], nums[index] # swap back
        
        backtrack(0)
        return arr

obj = Solution()
data = obj.permute(nums = [1,2,3])
#data = obj.permute(nums = [0,1])
#data = obj.permute(nums = [1])
print(data)