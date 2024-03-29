import io
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by end point   
        points.sort(key = lambda x: x[1])
        end = points[0][1]
        count = 1
        # iterate and count arrows
        for s,e in points[1:]:
            if s > end:
                count += 1
                end = e
        
        return count

obj = Solution()
#data = obj.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]])
#data = obj.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]])
data = obj.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]])
print(data)