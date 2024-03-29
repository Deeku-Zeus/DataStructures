import io
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0]
        stack = [(temperatures[-1],-1)]

        for i in range(2,len(temperatures)+1):
            while (stack) and (stack[-1][0] <= temperatures[-i]):
                stack.pop()
                
            stack.append((temperatures[-i],-i))

            if temperatures[-i] == stack[0][0]:
                answers.append(0)
            else:
                answers.append(stack[-2][1] - stack[-1][1])

        return reversed(answers)

obj = Solution()
#data = obj.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
#data = obj.dailyTemperatures(temperatures = [30,40,50,60])
data = obj.dailyTemperatures(temperatures = [30,60,90])
print(data)