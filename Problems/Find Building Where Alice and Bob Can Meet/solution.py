import io
from typing import List
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        mono_stack = []
        result = [-1 for _ in range(len(queries))]
        new_queries = [[] for _ in range(len(heights))]
        for i in range(len(queries)):
            a = queries[i][0]
            b = queries[i][1]
            if a > b:
                a, b = b, a
            if heights[b] > heights[a] or a == b:
                result[i] = b
            else:
                new_queries[b].append((heights[a], i))

        for i in range(len(heights) - 1, -1, -1):
            mono_stack_size = len(mono_stack)
            for a, b in new_queries[i]:
                position = self.search(a, mono_stack)
                if position < mono_stack_size and position >= 0:
                    result[b] = mono_stack[position][1]
            while mono_stack and mono_stack[-1][0] <= heights[i]:
                mono_stack.pop()
            mono_stack.append((heights[i], i))
        return result

    def search(self, height, mono_stack):
        left = 0
        right = len(mono_stack) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mono_stack[mid][0] > height:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans


obj = Solution()
#data = obj.leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]])
#data = obj.leftmostBuildingQueries(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]])
data = obj.leftmostBuildingQueries(heights = [972848101,52452333,824874411,11236854,96915303,664755843,683986672,20463230,849012547,537660277], queries = [[6,3],[1,4],[0,5],[0,4],[3,9],[7,0]])
print(data)