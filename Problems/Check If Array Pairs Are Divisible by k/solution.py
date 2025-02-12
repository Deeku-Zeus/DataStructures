import io
from typing import List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k
        
        for num in arr:
            remainder = (num % k + k) % k
            freq[remainder] += 1
        
        if freq[0] % 2 != 0:  
            return False
        
        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:  
                return False
        
        return True

obj = Solution()
#data = obj.canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5)
#data = obj.canArrange(arr = [1,2,3,4,5,6], k = 7)
data = obj.canArrange(arr = [1,2,3,4,5,6], k = 10)
print(data)