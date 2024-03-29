import io
from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        prev=0
        for i in bank:
            res=i.count('1')
            if res:
                ans+=prev*res
                prev=res
        return ans

obj = Solution()
#data = obj.numberOfBeams(bank = ["011001","000000","010100","001000"])
data = obj.numberOfBeams(bank = ["000","111","000"])
print(data)