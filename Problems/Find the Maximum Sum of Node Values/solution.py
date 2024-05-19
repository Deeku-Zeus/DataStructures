import io
from typing import List
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total_sum = 0
        positive_changes_count = 0
        smallest_positive_change = float("inf")
        largest_negative_change = float("-inf")

        for node_value in nums:
            xor_value = node_value ^ k
            total_sum += node_value
            change = xor_value - node_value

            if change > 0:
                smallest_positive_change = min(smallest_positive_change, change)
                total_sum += change
                positive_changes_count += 1
            else:
                largest_negative_change = max(largest_negative_change, change)

        if positive_changes_count % 2 == 0:
            return total_sum
        return max(total_sum - smallest_positive_change, total_sum + largest_negative_change)

obj = Solution()
#data = obj.maximumValueSum(nums = [1,2,1], k = 3, edges = [[0,1],[0,2]])
#data = obj.maximumValueSum(nums = [2,3], k = 7, edges = [[0,1]])
data = obj.maximumValueSum(nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]])
print(data)