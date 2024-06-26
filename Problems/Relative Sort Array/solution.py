import io
from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        bucket_indices = {}

        for i, e in enumerate(arr2):
            bucket_indices[e] = i

        buckets = [[] for _ in range(len(arr2))]
        end = []

        for e in arr1:
            if e not in bucket_indices:
                end.append(e)
            else:
                i = bucket_indices[e]
                buckets[i].append(e)
        
        end.sort()
        buckets_flatten = []
        
        for bucket in buckets:
            buckets_flatten += bucket
        
        return buckets_flatten + end

obj = Solution()
#data = obj.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6])
data = obj.relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6])
print(data)