import io
from typing import List
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        ans=[0]*n
        times=[0]*n
        meetings.sort()
        for start,end in meetings:
            flag=False
            minid=-1
            val=float('inf')
            for j in range(n):
                if times[j]<val:
                    val=times[j]
                    minid=j
                if times[j]<=start:
                    flag=True
                    ans[j]+=1
                    times[j]=end
                    break
            if not flag:
                ans[minid]+=1
                times[minid]+=(end-start)
        maxid=-1
        idx=-1
        for i in range(n):
            if ans[i]>maxid:
                maxid=ans[i]
                idx=i
        return idx

obj = Solution()
#data = obj.mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]])
data = obj.mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]])
print(data)