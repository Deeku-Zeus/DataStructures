import io
from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        
        if left == n - 1:
            return 0
        
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        result = min(n - left - 1, right)

        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
        
        return result

obj = Solution()
#data = obj.findLengthOfShortestSubarray(arr = [1,2,3,10,4,2,3,5])
#data = obj.findLengthOfShortestSubarray(arr = [5,4,3,2,1])
data = obj.findLengthOfShortestSubarray(arr = [1,2,3])
print(data)