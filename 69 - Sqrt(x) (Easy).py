class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            value = mid * mid
            if value == x:
                return mid
            elif value > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return right
            


            