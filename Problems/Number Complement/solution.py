import io
from typing import List
class Solution:
    def findComplement(self, num: int) -> int:
        def decimal_to_binary(n):
            if n == 0:
                return "0"
            binary = ""
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2
            return binary

        def binary_to_decimal(binary_str):
            decimal = 0
            binary_str = binary_str[::-1]  # Reverse the string to process from right to left
            for i in range(len(binary_str)):
                decimal += int(binary_str[i]) * (2 ** i)
            return decimal

        binary = decimal_to_binary(num)
        n = len(binary)

obj = Solution()
#data = obj.findComplement(num = 1)
#data = obj.findComplement(num = 2)
data = obj.findComplement(num = 5)
print(data)