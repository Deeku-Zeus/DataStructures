import io
from typing import List
from collections import defaultdict, deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        queue1 = deque([(1, None, root)])
        queue2 = []
        values = defaultdict(int)
        parents = defaultdict(int)
        parents[None] = root.val
        while queue1:           
            level, _, node = tree_node = queue1.popleft()    
            queue2.append(tree_node)       
            values[level] += node.val
            if node.left:
                parents[node] += node.left.val
                queue1.append((level + 1, node, node.left))
            if node.right:
                parents[node] += node.right.val
                queue1.append((level + 1, node, node.right))
        
        for level, parent, node in queue2:
            node.val = values[level] - parents[parent]
        return root

obj = Solution()
#data = obj.replaceValueInTree(root = [5,4,9,1,10,None,7])
data = obj.replaceValueInTree(root = [3,1,2])
print(data)