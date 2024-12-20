import io
from typing import List
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[10001] * n for _ in range(n)]
        
        # Initialize distance matrix
        for i in range(n):
            dist[i][i] = 0
        
        # Build initial graph
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w
        
        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        min_reachable_cities = n
        result = -1
        
        # Find the city with the smallest number of reachable cities
        for i in range(n):
            reachable_cities = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if reachable_cities <= min_reachable_cities:
                min_reachable_cities = reachable_cities
                result = i
        
        return result

obj = Solution()
#data = obj.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4)
data = obj.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2)
print(data)
