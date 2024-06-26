# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
import io
from collections import deque


class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) :
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(nl):
            ans=[]
            for i in nl:
                if i.isInteger():
                    ans.append(i.getInteger())
                else:
                    ans.extend(flatten(i.getList()))    
            return ans
        self.n=deque(flatten(nestedList))            
    
    def next(self) -> int:
        return self.n.popleft()
    
    def hasNext(self) -> bool:
         return self.n

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())