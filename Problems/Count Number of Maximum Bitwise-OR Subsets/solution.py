import io
from typing import Counter, List
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        pool = Counter()
        for curr in nums:
            pool[0] = 1
            for prev, times in [*pool.items()]:
                pool[prev|curr] += times
        return pool.most_common(1)[0][1]

obj = Solution()
#data = obj.countMaxOrSubsets(nums = [3,1])
#data = obj.countMaxOrSubsets(nums = [2,2,2])
data = obj.countMaxOrSubsets(nums = [3,2,1,5])
print(data)