import io
from collections import defaultdict
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        max_len = max(map(len, wordDict)) 
        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1): 
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]

obj = Solution()
#data = obj.wordBreak(s = "leetcode", wordDict = ["leet","code"])
#data = obj.wordBreak(s = "applepenapple", wordDict = ["apple","pen"])
data = obj.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])
print(data)