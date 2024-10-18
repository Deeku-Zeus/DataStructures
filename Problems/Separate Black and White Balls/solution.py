import io
from typing import List
class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0
        li = 0
        ri = len(s) - 1
        while li < ri:
            if s[li] == '1':
                if s[ri] == '0':
                    swaps += ri - li
                    li += 1
                ri -= 1
            else:
                if s[ri] == '1':
                    ri -= 1
                li += 1
        return swaps

obj = Solution()
#data = obj.minimumSteps(s = "101")
#data = obj.minimumSteps(s = "100")
data = obj.minimumSteps(s = "0111")
print(data)