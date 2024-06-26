import io
import math
from typing import List
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s=set()
        for i in range( 0, math.floor(math.sqrt(c)+1)):
            s.add(i*i)
            if  c-i*i in s or 2*i*i==c:
                return True
        return False

obj = Solution()
#data = obj.judgeSquareSum(c = 5)
data = obj.judgeSquareSum(c = 3)
print(data)