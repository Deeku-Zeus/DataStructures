import io
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        ans=0
        def helper(node):
            nonlocal ans
            if node==None:
                return
            helper(node.right)
            ans+=node.val
            node.val=ans
            helper(node.left)
        helper(root)  
        return root

obj = Solution()
#data = obj.bstToGst(root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
data = obj.bstToGst(root = [0,None,1])
print(data)