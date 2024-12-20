import io
from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Step 1: Calculate the total chalk usage in one round
        total_chalk = sum(chalk)
        
        # Step 2: Reduce k by the total chalk usage
        k %= total_chalk
        
        # Step 3: Find the student who needs to replace the chalk
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]

obj = Solution()
#data = obj.chalkReplacer(chalk = [5,1,5], k = 22)
data = obj.chalkReplacer(chalk = [3,4,1,2], k = 25)
print(data)