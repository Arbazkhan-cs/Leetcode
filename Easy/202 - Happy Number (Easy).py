class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(num):
            return sum(int(i)**2 for i in str(num))
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_sum(n)
        
        return n == 1