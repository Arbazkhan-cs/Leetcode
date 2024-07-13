class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        for i in range(int(math.sqrt(n)) + 2):
            if 2**i == n:
                return True
        return False