import io
from typing import List
from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        dq = deque()
        result = float('inf')

        for i in range(n + 1):
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                result = min(result, i - dq.popleft())


            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            dq.append(i)

        return result if result != float('inf') else -1

obj = Solution()
#data = obj.shortestSubarray(nums = [1], k = 1)
#data = obj.shortestSubarray(nums = [1,2], k = 4)
data = obj.shortestSubarray(nums = [2,-1,2], k = 3)
print(data)