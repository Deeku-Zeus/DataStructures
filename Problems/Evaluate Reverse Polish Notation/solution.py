import io
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens :
            if token == '+' :
                a , b = stack.pop() , stack.pop()
                stack.append( a + b ) 
            elif token == '-':
                a , b = stack.pop() , stack.pop()
                stack.append( b - a ) 
            elif token == '*':
                a , b = stack.pop() , stack.pop()
                stack.append( b * a ) 
            elif token == '/':
                a , b = stack.pop() , stack.pop()
                stack.append( int(b / a) ) 
            else:
                stack.append(int(token)) 
        return stack.pop()

obj = Solution()
#data = obj.evalRPN(tokens = ["2","1","+","3","*"])
#data = obj.evalRPN(tokens = ["4","13","5","/","+"])
data = obj.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(data)