import io
from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pass

obj = Solution()
#data = obj.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]])
data = obj.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]])
print(data)