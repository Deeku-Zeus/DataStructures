import io
from typing import List
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent={}
        for p,child in enumerate(zip(leftChild,rightChild)):
            for c in child:
                if c==-1:
                    continue 
                if c in parent:
                    return False 
                if p in parent and parent[p]==c:
                    return False 
                parent[c]=p
        root=set(range(n))-set(parent.keys())
        if  len(root)!=1:
            return False 
        def count(root):
            if root ==-1:
                return 0
            return  1+count(leftChild[root])+count(rightChild[root])
        return count(root.pop())==n


obj = Solution()
#data = obj.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1])
#data = obj.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1])
data = obj.validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1])
print(data)