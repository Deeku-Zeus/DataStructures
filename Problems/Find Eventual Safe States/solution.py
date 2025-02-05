import io
from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        safe={}
        ans=[]
        def dfs(i):
            if i in safe:
                return safe[i]

            safe[i]=False
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i]

            safe[i]=True
            return safe[i]

        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans
    


obj = Solution()
#data = obj.eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]])
data = obj.eventualSafeNodes(graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]])
print(data)