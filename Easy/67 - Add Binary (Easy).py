class Solution:
    def addBinary(self, a: str, b: str) -> str:
        digitA = int(a, 2)
        digitB = int(b, 2)

        total = digitA + digitB
        res = bin(total)[2:]
        return res