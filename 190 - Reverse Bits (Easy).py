class Solution:
    def reverseBits(self, n: int) -> int:
        # first way
        """
        bin_n = ""
        while n>0:
            rem = n % 2
            bin_n += str(rem)
            n //= 2
        
        res = int(bin_n, 2) if len(bin_n) == 32 else int(bin_n + "0"*(32-len(bin_n)), 2)
        return res
        """

        # second way
        res = 0
        for _ in range(32):
            res = (res<<1) + (n&1)
            n  = n >> 1
        
        return res