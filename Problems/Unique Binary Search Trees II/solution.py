from functools import lru_cache
import io
from collections import defaultdict
from typing import List
    # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[List[TreeNode]]:
        @lru_cache
        def dfs(start,end):
            if start>end:
                return [None]

            ans=[]
            for i in range(start,end+1):
                left=dfs(start,i-1)
                right=dfs(i+1,end)
                for l in left:
                    for r in right:
                        root=TreeNode(i)
                        root.left=l
                        root.right=r
                        ans.append(root)
            return ans

        return dfs(1,n)


obj = Solution()
data = obj.generateTrees(n = 3)
#data = obj.generateTrees(n = 1)
print(data)