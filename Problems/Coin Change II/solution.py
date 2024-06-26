import io
from typing import List
class Solution:
     def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1]

obj = Solution()
#data = obj.change(amount = 5, coins = [1,2,5])
#data = obj.change(amount = 3, coins = [2])
data = obj.change(amount = 10, coins = [10])
print(data)